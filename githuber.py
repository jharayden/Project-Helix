import os
import requests
import datetime
from dotenv import load_dotenv
from typing import Dict, Any
from openai import OpenAI
# Add these imports at the top of your file
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Bypass system proxies that might block the API
os.environ["NO_PROXY"] = "*"

class GitHuber:
    """
    V3.5 Microservice: GitHuber (The Open Source Trend Hunter)
    """
    def __init__(self):
        print("[SYSTEM] GitHuber Instantiated: Sensor Array Online.")
        # Initialize Cognitive Engine (GLM via OpenAI SDK)
        api_key = os.getenv("GLM_API_KEY")
        if not api_key:
            raise ValueError("[FATAL] GLM_API_KEY not found in .env file.")
        self.client = OpenAI(api_key=api_key, base_url="https://open.bigmodel.cn/api/paas/v4/")

    def hunt_top_lobster(self) -> Dict[str, Any]:
        """
        Phase 1: Sensor Layer. Scans for new repos in the last 7 days, 
        calculates velocity, and locks onto the Top 1.
        """
        print("\n[SENSOR LAYER] Scanning GitHub for the fastest-growing 'Lobster' in the last 7 days...")
        
        now = datetime.datetime.now(datetime.timezone.utc)
        seven_days_ago = (now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        
        query = f"created:>{seven_days_ago} ai OR agent OR automation OR plugin OR workflow"
        
        url = "https://api.github.com/search/repositories"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 30
        }
        
        headers = {"Accept": "application/vnd.github.v3+json"}
        github_token = os.getenv("GITHUB_TOKEN")
        if github_token:
            headers["Authorization"] = f"token {github_token}"
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            items = data.get("items", [])
            
            if not items:
                print("[ERROR] No targets found in the current window.")
                return {}

            print("[SENSOR LAYER] Applying Velocity Algorithm to top 30 targets...")
            
            best_repo = None
            max_velocity = -1.0
            
            for repo in items:
                created_at = datetime.datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00"))
                hours_alive = (now - created_at).total_seconds() / 3600.0
                velocity = repo["stargazers_count"] / (hours_alive + 1.0)
                
                if velocity > max_velocity:
                    max_velocity = velocity
                    best_repo = repo
            
            if not best_repo:
                return {}

            print(f"[SENSOR LAYER] Target Locked: {best_repo['full_name']}")
            print(f"               |> Stars: {best_repo['stargazers_count']} | Velocity: {max_velocity:.2f} stars/hr")
            
            readme_content = self._fetch_readme(best_repo['full_name'], headers)
            
            return {
                "name": best_repo["name"],
                "full_name": best_repo["full_name"],
                "html_url": best_repo["html_url"],
                "description": best_repo["description"] or "No description provided.",
                "language": best_repo["language"] or "Mixed/Unknown",
                "stars": best_repo["stargazers_count"],
                "readme": readme_content[:4000] 
            }

        except Exception as e:
            print(f"[ERROR] Sensor Layer Misfire: {e}")
            return {}

    def _fetch_readme(self, full_name: str, base_headers: dict) -> str:
        """
        Extracts raw Markdown text directly using GitHub's raw API format.
        """
        print(f"[SENSOR LAYER] Extracting README payload for {full_name}...")
        url = f"https://api.github.com/repos/{full_name}/readme"
        
        headers = base_headers.copy()
        headers["Accept"] = "application/vnd.github.v3.raw"
        
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                return r.text
            return "> [!error] No README available or failed to fetch."
        except:
            return "> [!error] Failed to extract README payload due to network error."

    def evaluate_lobster(self, lobster: Dict[str, Any]) -> str:
        """
        Phase 2: Cognitive Layer. Feeds the payload to the CTO Engine.
        """
        if not lobster:
            return ""
            
        print("\n[COGNITIVE LAYER] Waking up the CTO Engine (GLM)...")
        print(f"[COGNITIVE LAYER] Evaluating structural and commercial value of {lobster['name']}...")

        system_prompt = """
        Persona & Tone: You are a world-class Hacker, CTO, and AI Tech Lead. You communicate like a brilliant, friendly 20-something peer. You possess deep engineering intuition and commercial awareness, but you explain complex tech stacks and workflows using highly accessible, engaging, and easy-to-understand language. You are genuinely excited to share this new "killer app/repo" with your "bro/peer" (the user).

        Task & Constraints:
        - Analyze the provided README payload of today's fastest-growing GitHub repository.
        - Strip away the author's marketing fluff. I need the hard engineering truth and its real-world value.
        - Output strictly in Obsidian-flavored Markdown.
        - DYNAMIC TAGGING: Generate 2-3 specific hashtags based on the tech stack or use-case (e.g., #BrowserAutomation, #LocalLLM, #Productivity). Keep #GitHubHunter as a permanent tag.
        - Do not get lazy. Write thick, substantial, and highly detailed paragraphs for each section.

        Required Output Structure (STRICTLY FOLLOW THIS FORMAT):

        # 🦞 Today's Top Catch: [Repository Name]
        [Dynamic Tag 1] [Dynamic Tag 2] #GitHubHunter
        
        > [!info] 🎯 Target Locked
        > **Repo Link:** [Insert URL here]
        > **Tech Stack:** [e.g., Python, TypeScript, FastAPI, React]
        > **One-Line Pitch:** [1 sentence: What does this actually do?]
        
        > [!summary] 📦 1. Core Identity
        > [CRITICAL LENGTH: 2 paragraphs. Answer "是什么？". Strip the jargon. Explain the core mechanism, the architecture, and exactly what problem it solves. Is it a framework, a plugin, a UI, or a terminal tool? Explain it over a cup of coffee.]
        
        > [!example] 💎 2. The "Lobster" Value
        > [CRITICAL LENGTH: 1 thick paragraph. Answer "值什么？". Why is this trending so fast? Does it save exorbitant API costs? Does it replace a $20/month subscription? What is its commercial or extreme productivity potential?]
        
        > [!quote] 🛠️ 3. Deployment & Friction
        > [CRITICAL LENGTH: 1 thick paragraph. Answer "怎么用？". Be brutally honest about the developer experience (DX). Is it a 1-second `pip install` or a Docker compose nightmare? Give a concrete tip on how the user can spin this up with zero friction.]

        > [!abstract] ⚙️ 4. The Ideal Workflow & SOP
        > [CRITICAL LENGTH: 1 thick paragraph. Answer "理想工作流？". Paint a picture of the exact scenario where this shines. E.g., "Put this between your crawler and your database to automatically sanitize inputs..." How does this fit into a modern AI/Dev pipeline?]
        
        ---
        """

        user_prompt = f"""
        Target Repository: {lobster['full_name']}
        URL: {lobster['html_url']}
        Primary Language: {lobster['language']}
        Current Stars: {lobster['stars']}
        
        --- README PAYLOAD (Truncated to 4000 chars) ---
        {lobster['readme']}
        """

        try:
            # Using standard Zhipu API model name
            response = self.client.chat.completions.create(
                model="glm-4-plus", 
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            
            evaluation = response.choices[0].message.content
            print("[COGNITIVE LAYER] Evaluation complete. The CTO has spoken.")
            return evaluation
            
        except Exception as e:
            print(f"[ERROR] Cognitive Engine failure: {e}")
            return f"> [!error] Failed to evaluate {lobster['name']} due to API error."
            
    def save_to_vault(self, report: str) -> None:
        """
        Phase 3a: Storage Layer. Saves the raw Obsidian Markdown locally
        into a dedicated 'GitHuber' subfolder with collision-free filenames.
        """
        print("\n[STORAGE LAYER] Saving payload to Obsidian Vault...")
        base_vault_path = os.getenv("OBSIDIAN_PATH")
        if not base_vault_path or not os.path.exists(base_vault_path):
            print("[ERROR] OBSIDIAN_PATH is invalid or missing in .env.")
            return

        # V3.5 Routing: 自动在大文件夹下创建 'GitHuber' 专属子文件夹
        target_dir = os.path.join(base_vault_path, "GitHuber")
        os.makedirs(target_dir, exist_ok=True)

        today_str = datetime.date.today().strftime("%Y-%m-%d")
        counter = 1
        while True:
            filename = f"GitHuber_Catch_{today_str}_{counter}.md"
            full_path = os.path.join(target_dir, filename) # 存入专属子文件夹
            if not os.path.exists(full_path):
                break
            counter += 1

        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"[STORAGE LAYER] Success! Saved to: {full_path}")
        except Exception as e:
            print(f"[ERROR] Failed to save to Vault: {e}")

    def dispatch_email(self, report: str, repo_name: str) -> None:
        """
        Phase 3b: Dispatch Layer. Slices the Obsidian syntax and emails the payload.
        """
        print("\n[DISPATCH LAYER] Initializing Text Slicer and SMTP transmission...")
        sender = os.getenv("SENDER_EMAIL")
        password = os.getenv("EMAIL_PASSWORD")
        receiver = os.getenv("RECEIVER_EMAIL")

        if not all([sender, password, receiver]):
            print("[ERROR] Email credentials missing in .env.")
            return

        # Regex Slicer: Strip Obsidian callout syntax for clean plain text emails
        sliced_text = re.sub(r'^> \[\!.*?\] (.*?)$', r'--- \1 ---', report, flags=re.MULTILINE)
        sliced_text = re.sub(r'^> ', '', sliced_text, flags=re.MULTILINE)
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = f"🦞 GitHuber Alert: {repo_name} is Trending"

        msg.attach(MIMEText(sliced_text, 'plain', 'utf-8'))

        try:
            # FIXED: Added local_hostname="localhost" to bypass Windows GBK/UTF-8 decoding 
            # errors if the machine's hostname contains Chinese characters.
            server = smtplib.SMTP_SSL("smtp.163.com", 465, local_hostname="localhost") 
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()
            print("[DISPATCH LAYER] Payload successfully delivered to inbox!")
        except Exception as e:
            print(f"[ERROR] SMTP Transmission failed: {e}")
    

# Replace your current testing probe at the bottom with this final execution block
if __name__ == "__main__":
    githuber = GitHuber()
    
    # Phase 1: Hunt
    lobster = githuber.hunt_top_lobster()
    
    if lobster:
        # Phase 2: Evaluate
        report = githuber.evaluate_lobster(lobster)
        
        if report and not report.startswith("> [!error]"):
            print("\n" + "="*50)
            print("🚀 FINAL CTO REPORT GENERATED 🚀")
            print("="*50)
            
            # Phase 3: Action (Save & Send)
            githuber.save_to_vault(report)
            githuber.dispatch_email(report, lobster['name'])