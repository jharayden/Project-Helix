# 🧬 Project Helix: The Autonomous AI Intelligence Suite

![Version](https://img.shields.io/badge/Version-4.0.0_(Matrix)-00FF66.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688.svg?style=for-the-badge&logo=fastapi)
![Frontend](https://img.shields.io/badge/Frontend-Tailwind_|_Canvas-38B2AC.svg?style=for-the-badge)
![Brain](https://img.shields.io/badge/Brain-GLM--5-purple.svg?style=for-the-badge)

Welcome to **Project Helix v4.0: The Matrix Edition**. 

We didn't just update the UI; we fundamentally rewrote the architecture. Project Helix has evolved from a headless background script into a **Decoupled, High-Octane Single Page Application (SPA)**. It is your private, cyberpunk-styled intelligence dashboard designed to extract pure signal from the noise of academic research and open-source engineering.

Stop scrolling through abstract feeds. Ignite the engine, and let Helix hunt for you.

---

## 🚀 The Core DNA (V4.0 Arsenal)

We threw Streamlit out the window and built a custom FastAPI + HTML/JS/Canvas stack to achieve zero-latency interactions and cinematic visual effects.

- 🌧️ **Matrix Decryption Engine (NEW in V4.0):** A custom HTML5 Canvas rendering engine. When the AI thinks, your screen rains digital matrix code. Features a "Smart Braking System" that seamlessly fades the animation the exact millisecond your data arrives.
- 🧠 **SYNAPSE Core (The Copilot):** A built-in, GLM-powered conversational agent. You can now directly chat with the Helix AI. **Mount Intel** from your local Vault and ask the engine to analyze code, summarize papers, or evaluate commercial value in real-time. Features bulletproof null-state handling.
- 🗂️ **The Secure Vault:** A local intelligence library. Access all historical reports instantly within the browser. Features dynamic filtering (`ALL | ARXIV | GITHUB`), explosive GSAP `clip-path` transitions, and in-browser Markdown decryption.
- 🌅 **ARXIV Radar:** Scans the Arxiv database for the latest papers. The "Geek Professor" agent evaluates them and delivers the Top 3 theoretical breakthroughs. Intelligent routing defaults to your `.env` settings if left blank.
- 🌃 **GITHUB Catch:** Scans the GitHub API for the fastest-growing AI repositories. Calculates real-time growth velocity (`Stars / Hours Alive`). Leaves input blank? It automatically hunts the global top trending target.
- ⚡ **Shared Memory Architecture:** Seamlessly switch between Arxiv, Github, and Synapse tabs. The UI features state preservation—your search inputs and terminal outputs remain exactly as you left them when navigating between strands.

---
## 🛠️ Installation & Deployment (Foolproof Guide)

Welcome to Project Helix! Don't worry if you aren't a programmer or have never used a "terminal" before. If you can follow a cooking recipe, you can install this. Just follow these steps exactly as written.

### Phase 1: Install the Engine (Python)
Helix runs on a language called Python. We need to install it on your computer.
1. Go to the official website: **[python.org/downloads](https://www.python.org/downloads/)** and click the big yellow "Download Python" button.
2. Open the downloaded installer file.
3. 🚨 **CRITICAL STEP:** At the very bottom of the installation window, **CHECK THE BOX** that says **"Add python.exe to PATH"**. (If you skip this, nothing will work!)
4. Click "Install Now" and wait for it to finish.

### Phase 2: Download Project Helix
1. On this GitHub page, look for the green **"<> Code"** button near the top right.
2. Click it, then select **"Download ZIP"**.
3. Once downloaded, right-click the ZIP file and select **"Extract All..."**. 
4. Extract it to your Desktop so it's easy to find. Open the extracted folder so you can see all the files (like `api.py`, `index.html`, etc.).

### Phase 3: Get Your "Magic Keys" (Free!)
Helix needs an AI brain and an email account to send you reports. You need to get two secret passwords:

**1. The AI Brain Key (GLM-5):**
* Go to **[open.bigmodel.cn](https://open.bigmodel.cn/)** (Zhipu AI) and register for a free account.
* Click on your profile/dashboard and find the **"API Keys"** menu.
* Click "Create new API key" (or copy the default one). It will look like a long string of random letters and numbers. Keep this page open.

**2. The Email Dispatch Key (163 Mail):**
* *Note: Helix uses 163.com by default, but you can use others if you know how to configure SMTP.*
* Log into your 163 email account on the web.
* Go to **Settings** -> **POP3/SMTP/IMAP**.
* Turn **ON** the "SMTP Service". 
* It will ask you to verify your phone number and will then give you an **Authorization Code**. It usually looks like a 16-letter random password. 
* 🚨 *Never use your actual email login password! Only use this special Authorization Code.*

### Phase 4: Configure The Secret File (`.env`)
Now we need to put your keys into the Helix control panel.
1. In your extracted Helix folder, find the file named `.env.example`.
2. Right-click it, select **Rename**, and delete the `.example` part. It should now be named EXACTLY: `.env`
   *(Troubleshooting: If your computer hides file extensions and names it `.env.txt`, you need to go to View -> Show -> "File name extensions" in your Windows folder and fix it).*
3. Right-click your new `.env` file and select **"Open with" -> Notepad**.
4. Fill in the blanks with the keys you just got. It should look like this:
   ```text
   GLM_API_KEY="paste_your_long_zhipu_api_key_here"
   OBSIDIAN_PATH="C:/Users/YourName/Desktop/Helix_Vault"
   
   SENDER_EMAIL="your_email@163.com"
   EMAIL_PASSWORD="paste_your_16-letter_authorization_code_here"
   RECEIVER_EMAIL="where_you_want_to_receive_reports@gmail.com"
5. Save the file and close Notepad.

### Phase 5: Assembly (Opening the Terminal)
We need to download a few extra parts (libraries) to make the code run. 
1. Open your Helix folder (where `api.py` and your new `.env` file are).
2. Click directly on the **folder address bar** at the top of the window (where it says something like `C:\Users\Desktop\Helix`).
3. Delete all the text in the bar, type the letters **`cmd`**, and press **Enter**.
4. A black hacker-looking window (the Terminal) will pop up. Don't panic!
5. Copy and paste the exact text below into the black window and press **Enter**:
   ```bash
   pip install -r requirements.txt
6. You will see a lot of text scrolling by. Wait for it to stop and say "Successfully installed...". This means your engine is ready.

### Phase 6: IGNITION! 🚀
You only have to do Phases 1-5 once. From now on, whenever you want to use Helix, just do this:
1. Open the black `cmd` terminal in your folder again (Repeat Phase 5, steps 1-3).
2. Type this command and press **Enter**:
   ```bash
   python api.py
3.If it says "Igniting Project Helix Backend...", leave this black window open in the background. It is the engine running.
4.Finally, double-click the index.html file in your folder. Your web browser will open the Helix Command Center.

You are now officially jacked into the Matrix. Click IGNITE and watch the magic happen!
---

## ☁️ Cloud Autopilot (GitHub Actions)
Helix still supports fully autonomous nightly dispatching via GitHub Actions.
Configure `.github/workflows/daily_hunt.yml` and `githuber.yml` with your repository secrets to receive CTO-level briefings directly to your Email without keeping your PC on.

---

## 🗺️ Roadmap

- [x] **V2.0:** Base LLM integration, SMTP setup, and daily automation via Actions.
- [x] **V3.5:** Velocity Radar, CTO Persona, Smart Folder Routing.
- [x] **V3.6.0 (The UI Overhaul):** Complete front-end/back-end separation (FastAPI + JS). Implementation of **SYNAPSE Copilot**, GSAP Animations, Local Vault Reader, and State Memory.
- [x] **V4.0.0 (The Matrix Edition):** Cinematic data-driven code rain, intelligent UI braking system, robust `.env` vs UI payload routing, and foolproof empty-state handling.
- [ ] **V4.1.0 (Accessibility & Localization):** Create a one-click `.bat`/`.command` boot script (Zero-Terminal startup) and an "Elderly-Friendly" Chinese translation mode.
- [ ] **V5.0.0 (Native Desktop):** Transform the SPA into a standalone desktop application using Tauri + React/Vue architecture.

---
*Built with excessive amounts of coffee, zero sleep, and a refusal to read bad papers manually.*