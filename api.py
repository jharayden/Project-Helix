import os
import shutil
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
raw_path = os.getenv("OBSIDIAN_PATH", "").strip()

# 1. 兜底逻辑：确定总仓位置
if raw_path:
    MASTER_VAULT = raw_path
else:
    MASTER_VAULT = os.path.join(BASE_DIR, "Vault")

os.makedirs(MASTER_VAULT, exist_ok=True)
print(f"[SYSTEM] Core Vault synchronized at: {MASTER_VAULT}")

# [偷天换日的核心！] 强行把确定好的路径塞回系统环境变量里！
# 这样一来，你 api.py 下面的所有接口，以及 hunter.py 和 githuber.py，
# 读取 os.getenv("OBSIDIAN_PATH") 时，拿到的都是这个绝对正确的路径！
os.environ["OBSIDIAN_PATH"] = MASTER_VAULT

# 2. 自动搬运工：把 git pull 拉回来的文件，塞进总仓！
for folder in ["Arxiv_Papers", "GitHuber"]:
    cloud_folder = os.path.join(BASE_DIR, folder)
    target_folder = os.path.join(MASTER_VAULT, folder)
    
    # 如果根目录有云端拉下来的文件夹
    if os.path.exists(cloud_folder):
        os.makedirs(target_folder, exist_ok=True)
        # 遍历里面的 .md 文件
        for file_name in os.listdir(cloud_folder):
            if file_name.endswith(".md"):
                cloud_file = os.path.join(cloud_folder, file_name)
                target_file = os.path.join(target_folder, file_name)
                # 如果总仓里还没有这个文件，就复制过去
                if not os.path.exists(target_file):
                    shutil.copy2(cloud_file, target_file)
                    print(f"[SYNC] Moved cloud intelligence to vault: {file_name}")
# =================================================================

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

@app.post("/api/arxiv/ignite")
async def trigger_arxiv_hunter(request: HuntRequest):
    """
    Morning Academic Radar (Arxiv) - APN Protocol Enabled
    """
    try:
        actual_topic = request.target_topic.strip()
        if not actual_topic:
            actual_topic = os.getenv("TARGET_TOPIC")
        api_key = os.getenv("GLM_API_KEY")
        obsidian_path = os.getenv("OBSIDIAN_PATH")
        
        hunter = ArxivHunter(glm_api_key=api_key)
        
        # 1. GENERATE: Execute LLM Pipeline
        papers = hunter.hunt_papers(query=request.target_topic, max_results=10)
        report = hunter.digest_papers(papers=papers)
        
        if not report or report.startswith("> [!error]"):
            raise HTTPException(status_code=500, detail="Cognitive Layer Misfire: Failed to generate report.")

        # 2. SAVE: Persist to Obsidian Vault (Atomic Step 1)
        try:
            hunter.save_report(content=report, vault_path=obsidian_path)
            print("[HELIX_ROUTING] Successfully saved Arxiv report to Vault.")
        except Exception as e:
            print(f"[HELIX_ERROR] Vault Persistence Failed: {e}")
            # We don't block the email if Vault fails, but we log it heavily.

        # 3. DISPATCH: Send SMTP Email (Atomic Step 2)
        try:
            # Assuming your ArxivHunter has a method for email. Adjust method name if needed.
            hunter.send_email(report) 
            print("[HELIX_ROUTING] Successfully dispatched Arxiv SMTP email.")
        except Exception as e:
            print(f"[HELIX_ERROR] SMTP Dispatch Failed: {e}")

        return {"status": "success", "payload": report}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Arxiv Pipeline Error: {str(e)}")

@app.post("/api/github/ignite") 
async def trigger_github_radar(request: HuntRequest):
    """
    Nightly Open-Source Radar (GitHub) - APN Protocol Enabled
    """
    try:
        actual_topic = request.target_topic.strip()
        githuber = GitHuber()
        
        # 1. TARGET & GENERATE
        lobster = githuber.hunt_top_lobster(query=actual_topic) 
        if not lobster:
            raise HTTPException(status_code=404, detail="No targets locked for this sector.")
            
        report = githuber.evaluate_lobster(lobster)
        
        if not report or report.startswith("> [!error]"):
            raise HTTPException(status_code=500, detail="CTO Engine Misfire: Evaluation failed.")

        # 2. SAVE: Persist to Obsidian Vault (Atomic Step 1)
        try:
            githuber.save_to_vault(report)
            print(f"[HELIX_ROUTING] Successfully saved Lobster '{lobster['name']}' to Vault.")
        except Exception as e:
            print(f"[HELIX_ERROR] Vault Persistence Failed for GitHuber: {e}")

        # 3. DISPATCH: Send SMTP Email (Atomic Step 2)
        try:
            # Assuming your GitHuber has a method for email. Adjust method name if needed.
            githuber.send_email(report, lobster["name"]) 
            print(f"[HELIX_ROUTING] Successfully dispatched GitHub SMTP email for '{lobster['name']}'.")
        except Exception as e:
            print(f"[HELIX_ERROR] SMTP Dispatch Failed for GitHuber: {e}")

        return {"status": "success", "target": lobster["name"], "payload": report}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GitHub Pipeline Error: {str(e)}")

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
from typing import Optional # 如果没有导包，记得在文件最上面加一下

class ChatRequest(BaseModel):
    message: str
    history: list
    context_path: Optional[str] = None  # <--- 改成这行！允许它为空！(或者写 context_path: str | None = None)

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