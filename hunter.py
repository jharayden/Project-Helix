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
        Phase 2: Hunt. Executes API GET requests to Arxiv Sort by SubmittedDate[cite: 19].
        Returns a list of raw metadata (Title, Abstract, Authors)[cite: 19].
        """
        print(f"[ACTION LAYER] Executing search query: '{query}'...")
        
        # Deterministic execution using the arxiv library
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
                "Published": str(paper.published)
            }
            results.append(paper_data)
        
        print(f"[ACTION LAYER] Successfully retrieved {len(results)} papers.")
        return results

    def digest_papers(self, papers: List[Dict[str, str]]) -> str:
        """
        Phase 3: Digest. Constructs context payload and prompts GLM-5 
        to evaluate structural novelty and output Obsidian MD.
        """
        print("[COGNITIVE LAYER] Initializing semantic analysis and structural evaluation...")
        
        if not papers:
            return "> [!error] No papers found in the telemetry payload."

        # 1. Context Assembly: Convert dictionary list into a structured string payload.
        payload = ""
        for i, p in enumerate(papers, 1):
            payload += f"\n--- Paper {i} ---\nTitle: {p['Title']}\nAuthors: {p['Authors']}\nAbstract: {p['Abstract']}\n"
            
        # 2. Prompt Engineering: Strictly defining the Persona and Output constraints.
        system_prompt = """
        You are a world-class Professor of Artificial Intelligence and Embodied AI. However, you do not speak like a dusty, arrogant academic. You communicate like a brilliant, friendly 20-something peer. You possess deep, top-tier academic expertise, but you explain complex concepts using highly accessible, engaging, and easy-to-understand language. You are genuinely excited to share knowledge with your "bro/peer" (the user).

        Task & Constraints:
        1. Filtering: Analyze the provided context payload (Titles, Abstracts, Authors) of recent Arxiv submissions. Select the SINGLE MOST VALUABLE paper based on structural novelty and industry potential in Embodied AI. Ignore the noise.
        2. Formatting: You MUST strictly output your analysis using Obsidian-flavored Markdown source code. Use Obsidian callouts (e.g., `> [!info]`, `> [!summary]`, `> [!quote]`), bolding, and `#tags` to make the output visually stunning when rendered in an Obsidian vault.

        Required Output Structure (Strictly follow this Obsidian MD format):
        # [Insert Paper Title Here]
        #EmbodiedAI #DailyPaper #ArxivHunter

        > [!info] Target Locked
        > **Authors:** [Insert Authors]
        > **Why this one?** [1-sentence, enthusiastic justification for why you picked this specific paper today.]

        > [!summary] Core Innovation (The "Bro, what does this actually do?" Section)
        > [Strip away the academic jargon. Explain the underlying mechanics and what specific problem it solves in plain, friendly language.]

        > [!example] Value Assessment & Future Prospects
        > [What is the future impact of this technology? How can this be applied in real-world robotics or AI industry scenarios?]

        > [!quote] Professor's Deep Dive
        > [Provide your critical, independent thought on this paper. Is there a hidden flaw? Is it a game-changer or just an incremental update? Keep the tone sharp but peer-to-peer.]
        """
        
        # 3. Deterministic API Execution: Routing to GLM-5 with Deep Thinking.
        try:
            response = self.llm_client.chat.completions.create(
                model="glm-5",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context Payload:\n{payload}"}
                ],
                temperature=1.0, # Adjusted to 1.0 as per GLM-5 official docs for thinking mode
                extra_body={"thinking": {"type": "enabled"}} # Injecting the cognitive afterburner
            )
            
            # Extracting the standard response (we bypass the raw thinking process for the final report)
            synthesis = response.choices[0].message.content
            print("[COGNITIVE LAYER] Semantic analysis complete. Obsidian MD generated.")
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
    retrieved_papers = hunter.hunt_papers(query="Embodied AI", max_results=5)
    
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