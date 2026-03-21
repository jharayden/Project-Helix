import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path

# Import our V3.5 Dual-Strand Engines
from hunter import ArxivHunter
from githuber import GitHuber
from openai import OpenAI

# Load secure credentials
load_dotenv()
os.environ["NO_PROXY"] = "*"

# Initialize FastAPI Core
app = FastAPI(title="Project Helix API", version="3.6.0")

# [CRITICAL FIX] Bypass browser CORS policy for local HTML UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Data Models
class HuntRequest(BaseModel):
    target_topic: str = "Embodied AI"

# --- API Endpoints ---

@app.get("/api/health")
async def health_check():
    """
    Diagnostic endpoint to verify server status.
    """
    return {"status": "Helix Backend Online", "code": 200}

@app.post("/api/arxiv/ignite") # [RENAMED] Strand A -> Arxiv
async def trigger_arxiv_hunter(request: HuntRequest):
    """
    Morning Academic Radar (Arxiv)
    """
    try:
        api_key = os.getenv("GLM_API_KEY")
        obsidian_path = os.getenv("OBSIDIAN_PATH")
        
        hunter = ArxivHunter(glm_api_key=api_key)
        papers = hunter.hunt_papers(query=request.target_topic, max_results=10)
        report = hunter.digest_papers(papers=papers)
        
        if report and not report.startswith("> [!error]"):
            hunter.save_report(content=report, vault_path=obsidian_path)
            return {"status": "success", "payload": report}
        else:
            raise HTTPException(status_code=500, detail="Cognitive Layer Misfire.")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/github/ignite") 
async def trigger_github_radar(request: HuntRequest): # [NEW] 1. 接收前端传来的 request (包含关键词)
    """
    Nightly Open-Source Radar (GitHub) - Targeted Search Enabled
    """
    try:
        githuber = GitHuber()
        
        # [NEW] 2. 将前端传来的关键词 (target_topic)，喂给寻龙虾引擎！
        # 注意：这里我们传入了 query 参数
        lobster = githuber.hunt_top_lobster(query=request.target_topic) 
        
        if not lobster:
            raise HTTPException(status_code=404, detail="No targets locked for this sector.")
            
        report = githuber.evaluate_lobster(lobster)
        
        if report and not report.startswith("> [!error]"):
            githuber.save_to_vault(report)
            return {"status": "success", "target": lobster["name"], "payload": report}
        else:
            raise HTTPException(status_code=500, detail="CTO Engine Misfire.")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/vault/list") # [NEW ENDPOINT] To list files
async def list_vault_files():
    """
    Scan Obsidian Vault for historical reports.
    """
    try:
        vault_base = os.getenv("OBSIDIAN_PATH")
        if not vault_base or not os.path.exists(vault_base):
            return {"arxiv_papers": [], "github_repos": []}
            
        arxiv_path = Path(vault_base) / "Arxiv_Papers"
        github_path = Path(vault_base) / "GitHuber"
        
        arxiv_files = []
        if arxiv_path.exists():
            for file_path in arxiv_path.glob("Arxiv_Hunter_*.md"):
                arxiv_files.append({"name": file_path.name, "path": str(file_path)})
            arxiv_files.sort(key=lambda x: x["name"], reverse=True) # newest first
                
        github_files = []
        if github_path.exists():
            # [BUG FIX] 放宽匹配规则，抓取 GitHuber 文件夹下所有的 Markdown 战报
            for file_path in github_path.glob("*.md"): 
                github_files.append({"name": file_path.name, "path": str(file_path)})
            github_files.sort(key=lambda x: x["name"], reverse=True) # newest first

        return {"arxiv_papers": arxiv_files, "github_repos": github_files}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/vault/read") # [NEW ENDPOINT] To read a file
async def read_vault_file(path: str):
    """
    Read content of a specific local markdown file.
    """
    try:
        if not os.path.exists(path) or not path.endswith('.md'):
             raise HTTPException(status_code=404, detail="Intel File Not Found.")
             
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"content": content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- [NEW] SYNAPSE CHAT ENGINE ---
class ChatRequest(BaseModel):
    message: str
    history: list = []
    context_path: str = None

@app.post("/api/chat")
async def helix_chat(request: ChatRequest):
    """
    SYNAPSE Core: Direct chat with GLM-5, with optional Vault context.
    """
    try:
        api_key = os.getenv("GLM_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="GLM_API_KEY missing.")
            
        client = OpenAI(api_key=api_key, base_url="https://open.bigmodel.cn/api/paas/v4/")
        
        # 1. 铸造系统级认知 Prompt
        system_prompt = "You are Project Helix (SYNAPSE), an elite Senior AI Architect and research assistant. Answer precisely, deeply, and functionally in Markdown."
        
        # 2. 如果用户挂载了 Vault 里的机密文件，强行注入上下文！
        if request.context_path and os.path.exists(request.context_path):
            with open(request.context_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            system_prompt += f"\n\n[CLASSIFIED CONTEXT FROM VAULT]:\n{file_content}\n\nAnalyze and answer based on the context above."
        
        # 3. 组装记忆链
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(request.history)
        messages.append({"role": "user", "content": request.message})
        
        # 4. 点火大模型
        response = client.chat.completions.create(
            model="glm-4", # 智谱API目前通用模型代号
            messages=messages,
            temperature=0.7
        )
        
        return {"status": "success", "reply": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("[SYSTEM] Igniting Project Helix Backend API v3.6...")
    uvicorn.run(app, host="127.0.0.1", port=8000)