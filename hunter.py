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
            
        # 2. V3.1.2 Prompt Engineering: Persona + Anti-Laziness & Strict Depth Constraints
        system_prompt = """
        Persona & Tone: You are a world-class Professor of high-end technology, such as Embodied AI, Robotics, and LLMs. However, you do not speak like a dusty, arrogant academic. You communicate like a brilliant, friendly 20-something peer. You possess deep, top-tier academic expertise, but you explain complex concepts using highly accessible, engaging, and easy-to-understand language. You are genuinely excited to share knowledge with your "bro/peer" (the user).

        Task & Constraints:
        - Analyze the ENTIRE provided context payload of recent papers. 
        - EXACTLY 3 PAPERS: You MUST select EXACTLY the TOP 3 most valuable papers based on structural novelty and industry potential. Do not output just 1 or 2; I need exactly 3.
        - NO TRUNCATION: You must maintain the exact same extreme technical depth, length, and quality for Top 2 and Top 3 as you do for Top 1. Do not get lazy.
        - Output strictly in Obsidian-flavored Markdown.
        - DYNAMIC TAGGING: Generate 2-3 specific hashtags based on the paper's actual content. Keep #ArxivHunter as a permanent tag.
        - URL REQUIREMENT: You MUST include the exact URL provided in the payload for each selected paper.

        Required Output Structure (STRICTLY REPEAT THIS ENTIRE BLOCK 3 TIMES, for Top 1, Top 2, and Top 3):

        # 🥇 Top [1/2/3]: [Paper Title]
        [Dynamic Tag 1] [Dynamic Tag 2] #ArxivHunter
        
        > [!info] 🎯 Target Locked
        > **Authors:** [Authors]
        > **Link:** [Insert URL here - Crucial for Zotero!]
        > **Why this one, bro?:** [1-2 sentence, enthusiastic justification for why you picked this specific paper today.]
        
        > [!summary] 💡 Core Innovation
        > [CRITICAL LENGTH: Write 2-3 substantial paragraphs here. Strip away the academic jargon. Explain the underlying mechanics, the math/logic, and what specific problem it solves in plain, friendly language (as if explaining it over a cup of coffee), while maintaining extreme technical depth.]
        
        > [!example] 📈 Value Assessment & Future Prospects
        > [CRITICAL LENGTH: Write a highly detailed paragraph. What is the future impact of this technology? How can this be applied in real-world robotics or AI industry scenarios?]
        
        > [!quote] 🧠 Professor's Deep Dive
        > [CRITICAL LENGTH: Write a highly detailed paragraph. Provide your critical, independent thought on this paper. Is there a hidden flaw? Is it a game-changer or just an incremental update? Keep the tone sharp but peer-to-peer.]
        
        ---
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model="glm-5", # Note: using glm-5 as base endpoint per standard, but it routes to the latest model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context Payload:\n{payload}"}
                ],
                temperature=1.0, 
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
        
        # V3.5 Routing: 自动在大文件夹下创建 'Arxiv_Papers' 专属子文件夹
        target_dir = os.path.join(vault_path, "Arxiv_Papers")
        os.makedirs(target_dir, exist_ok=True)
            
        # --- V3.1.6 Auto-Increment Filename System ---
        today_str = datetime.date.today().strftime("%Y-%m-%d")
        
        # 碰撞检测循环：从 1 开始试，如果有重复的就 +1，直到找到空位
        counter = 1
        while True:
            filename = f"Arxiv_Hunter_{today_str}_{counter}.md"
            # 注意：这里的路径拼接换成了 target_dir
            full_path = os.path.join(target_dir, filename) 
            if not os.path.exists(full_path):
                break  # 找到没人占用的名字了，跳出循环！
            counter += 1
        # ----------------------------------------------
        
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

            # --- THE TEXT SLICER V3.1.5 (Full Content, No Truncation) ---
            import re
            clean_text = content
            
            # 1. Regex Translation: 完美同步你 Prompt 里的极客文案和 Emoji
            clean_text = re.sub(r'> \[!info\].*', '🎯 [TARGET LOCKED]', clean_text)
            clean_text = re.sub(r'> \[!summary\].*', '💡 [CORE INNOVATION]', clean_text)
            clean_text = re.sub(r'> \[!example\].*', '📈 [VALUE ASSESSMENT & PROSPECTS]', clean_text)
            clean_text = re.sub(r'> \[!quote\].*', '🧠 [PROFESSOR\'S DEEP DIVE]', clean_text)
            
            # 2. 扒掉剩下正文内容的 blockquote 箭头
            clean_text = clean_text.replace("> ", "")
            
            # 3. Dynamic Subject Line Update
            try:
                first_tag = re.search(r'#(\w+)', content).group(1)
            except:
                first_tag = "Latest Research"
            msg['Subject'] = f"🤖 Arxiv Hunter [{first_tag}]: {today_str}"

            # 4. 彻底移除截断逻辑！直接将满血清洗后的三篇完整长文塞进邮件！
            short_email_text = clean_text

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
    # 【V2.1.1 终极防御补丁】：不仅防丢失，还要防空字符串！
    target_topic = os.getenv("TARGET_TOPIC")
    if not target_topic:  # 如果是 None 或者 ""，全部判定为失效
        target_topic = "Embodied AI"

    print(f"\n--- INITIATING HUNT SEQUENCE FOR: {target_topic} ---")
    
    # 【V2.1 修改】：把写死的 "Embodied AI" 换成动态变量 target_topic
    retrieved_papers = hunter.hunt_papers(query=target_topic, max_results=15)
    
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