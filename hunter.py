import os
import urllib.request
import datetime # NEW: Required for dynamic daily filenames
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# The Nuclear Bypass: Completely blind Python to Windows Registry proxies
os.environ["NO_PROXY"] = "*"
urllib.request.getproxies = lambda: {} # Force return empty proxy dict

import arxiv
from openai import OpenAI
from typing import List, Dict

class ArxivHunter:
    """
    The Orchestrator (Control Layer): Dictates the standard operating procedure (SOP).
    """
    def __init__(self, glm_api_key: str) -> None:
        # Action Layer (Sensors): The deterministic interface to query the Arxiv database.
        self.arxiv_client = arxiv.Client()
        
        # Cognitive Layer (Brain): The GLM-5 API configuration[cite: 15].
        # Must use the exact base_url to route to Zhipu AI[cite: 22].
        self.llm_client = OpenAI(
            api_key=glm_api_key,
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )
        print("[SYSTEM] Arxiv Hunter Instantiated: Telemetry Online.")

    def hunt_papers(self, query: str, max_results: int = 3) -> List[Dict[str, str]]:
        """
        Phase 2: Hunt. Executes API GET requests to Arxiv.
        Now upgraded to extract direct URLs for Zotero integration.
        """
        print(f"[ACTION LAYER] Executing search query: '{query}'...")
        
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        results: List[Dict[str, str]] = []
        for paper in self.arxiv_client.results(search):
            paper_data = {
                "Title": paper.title,
                "Authors": ", ".join([author.name for author in paper.authors]),
                "Abstract": str(paper.summary).replace('\n', ' '),
                "Published": str(paper.published),
                "URL": paper.entry_id  # <--- V2.0 NEW: 抓取官方原版链接!
            }
            results.append(paper_data)
            
        print(f"[ACTION LAYER] Successfully retrieved {len(results)} papers.")
        return results

    def digest_papers(self, papers: List[Dict[str, str]]) -> str:
        """
        Phase 3: Digest. V2.0 Engine.
        Evaluates up to 20 papers, selects Top 3, provides deep tech-dive and URLs.
        """
        print("[COGNITIVE LAYER] Initializing V2.0 semantic analysis (Top 3 Selection)...")
        
        if not papers:
            return "> [!error] No papers found in the telemetry payload."

        # 1. Context Assembly (Now includes URLs)
        payload = ""
        for i, p in enumerate(papers, 1):
            payload += f"\n--- Paper {i} ---\nTitle: {p['Title']}\nAuthors: {p['Authors']}\nURL: {p['URL']}\nAbstract: {p['Abstract']}\n"
            
        # 2. V2.0 Prompt Engineering: Demanding Top 3 and extreme depth.
        system_prompt = """
        You are a world-class AI researcher and a brilliant, friendly peer. Your user relies on you to filter the daily noise of Arxiv.
        
        Task: 
        Analyze the provided payload of recent papers. You MUST select the TOP 3 most valuable papers based on structural novelty, empirical results, and industry impact. Ignore the incremental/boring ones.
        
        Constraints:
        - Output strictly in Obsidian-flavored Markdown.
        - You MUST include the exact URL provided in the payload for each selected paper.
        - Provide deep, technical analysis. Do not just summarize; evaluate the methodology and its real-world implications.
        
        Required Output Structure (Repeat this block for all 3 papers):
        
        # 🥇 Top 1: [Paper Title]
        #EmbodiedAI #ArxivHunter
        
        > [!info] Meta Data
        > **Authors:** [Authors]
        > **Link:** [Insert URL here - Crucial for Zotero!]
        > **Why Top 1:** [1-2 sentences on why this is the best paper today.]
        
        > [!summary] Core Innovation & Architecture
        > [Deep dive: Explain the model architecture, the math/logic behind it, and what makes it structurally novel. Use accessible but highly technical language.]
        
        > [!example] Real-world Impact & Limitations
        > [Where can this be deployed? What are the bottleneck or limitations the authors aren't saying loudly?]
        
        ---
        (Then do 🥈 Top 2 and 🥉 Top 3 following the exact same structure).
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model="glm-4", # Note: using glm-4 as base endpoint per standard, but it routes to the latest model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context Payload:\n{payload}"}
                ],
                temperature=0.4, 
                extra_body={"thinking": {"type": "enabled"}} 
            )
            
            synthesis = response.choices[0].message.content
            print("[COGNITIVE LAYER] V2.0 Deep analysis complete.")
            return synthesis
        except Exception as e:
            print(f"[ERROR] Cognitive Layer misfire: {e}")
            return f"> [!error] System Failure during Cognitive processing: {e}"

    def save_report(self, content: str, vault_path: str) -> None:
        """
        Phase 4: Report. Writes the synthesized AI response to the local file system.
        """
        print(f"\n[ORCHESTRATOR] Initiating Phase 4: Writing telemetry to local vault...")
        
        # Ensure the directory exists
        if not os.path.exists(vault_path):
            os.makedirs(vault_path)
            
        # Generate a dynamic filename based on today's date
        today_str = datetime.date.today().strftime("%Y-%m-%d")
        filename = f"Arxiv_Hunter_{today_str}.md"
        full_path = os.path.join(vault_path, filename)
        
        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[ORCHESTRATOR] SUCCESS! Report securely saved to: {full_path}")
        except Exception as e:
            print(f"[ERROR] Action Layer failed to write file: {e}")

    def dispatch_email(self, content: str, sender_email: str, app_password: str, receiver_email: str, smtp_server: str, smtp_port: int = 465) -> None:
        """
        Phase 4 (Action B): Deterministic SMTP client. 
        Zero dependencies. Cleans and slices the content for a quick email read.
        """
        print(f"\n[ORCHESTRATOR] Initiating Phase 4 (Action B): Slicing text for email dispatch...")
        
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            
            today_str = datetime.date.today().strftime("%Y-%m-%d")
            msg['Subject'] = f"🤖 Arxiv Hunter Alert: Embodied AI ({today_str})"

            # --- THE TEXT SLICER (Pure Python, No pip needed) ---
            # 1. Clean up the messy Obsidian tags to make it plain-text friendly
            clean_text = content.replace("> [!info] Target Locked", "🎯 [TARGET LOCKED]")
            clean_text = clean_text.replace("> [!summary] Core Innovation (The \"Bro, what does this actually do?\" Section)", "\n💡 [CORE INNOVATION]")
            clean_text = clean_text.replace("> [!example] Value Assessment & Future Prospects", "\n📈 [VALUE PROSPECTS]")
            clean_text = clean_text.replace("> [!quote] Professor's Deep Dive", "\n🧠 [DEEP DIVE]")
            clean_text = clean_text.replace("> ", "") # Remove blockquote arrows
            
            # 2. Slice the content to make it shorter for the email (Optional refinement)
            # We will split the text and drop the heavy "Deep Dive" section for the quick email read.
            if "🧠 [DEEP DIVE]" in clean_text:
                short_email_text = clean_text.split("🧠 [DEEP DIVE]")[0]
                short_email_text += "\n\n(For the Professor's Full Deep Dive, check your Obsidian Vault!)"
            else:
                short_email_text = clean_text
            # ----------------------------------------------------

            # Attach the clean, shortened text
            msg.attach(MIMEText(short_email_text, 'plain', 'utf-8'))

            # Execute SMTP transmission (Bypassing Windows Hostname Bug)
            server = smtplib.SMTP_SSL(smtp_server, smtp_port, local_hostname='localhost')
            server.login(sender_email, app_password)
            server.send_message(msg)
            server.quit()
            
            print(f"[ORCHESTRATOR] SUCCESS! Target acquired. Clean Email dispatched to {receiver_email}.")
        except Exception as e:
            print(f"[ERROR] Action Layer failed to dispatch email: {e}")


if __name__ == "__main__":
    # --- 1. SYSTEM CONFIGURATION ---
    
    # 第一步：激活保险箱！
    load_dotenv()
    
    # 第二步：安全读取机密信息 (OS 会自动去 .env 文件里找对应的值)
    api_key = os.getenv("GLM_API_KEY")
    obsidian_path = os.getenv("OBSIDIAN_PATH")
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    # 邮箱服务器是公开的地址，不需要保密
    smtp_server = "smtp.163.com" 
    
    # Ignite the Orchestrator
    hunter = ArxivHunter(glm_api_key=api_key)
    
    # --- 2. THE AUTONOMOUS LOOP ---
    print("\n--- INITIATING HUNT SEQUENCE ---")
    # V2.0: 扩大漏斗，一口气抓 15 篇让 AI 慢慢挑！
    retrieved_papers = hunter.hunt_papers(query="Embodied AI", max_results=15)
    
    print("\n--- INITIATING COGNITIVE DIGEST ---")
    final_report = hunter.digest_papers(papers=retrieved_papers)
    
    # Execute Phase 4 (Write to Disk -> Dispatch to Phone)
    if not final_report.startswith("> [!error]"):
        hunter.save_report(content=final_report, vault_path=obsidian_path)
        
        hunter.dispatch_email(
            content=final_report, 
            sender_email=sender_email, 
            app_password=app_password, 
            receiver_email=receiver_email, 
            smtp_server=smtp_server
        )
    else:
        print("[ORCHESTRATOR] Aborting Phase 4 due to Cognitive Layer error.")
        
    print("\n[SYSTEM] Arxiv Hunter routine complete. Mission Accomplished. Entering standby.")