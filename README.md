# 🧬 Project Helix: The Autonomous AI Intelligence Suite

Welcome to **Project Helix v5.0: The Desktop Matrix Edition**.

We didn't just update the UI; we fundamentally rewrote the reality of this application. Project Helix has evolved from a headless background script into a **Standalone, Borderless Windows Desktop Application**. It is your private, cyberpunk-styled intelligence dashboard designed to extract pure signal from the noise of academic research and open-source engineering—all without ever opening a terminal.

Stop scrolling through abstract feeds. Double-click the icon, ignite the engine, and let Helix hunt for you.

---

## 🚀 The Core DNA (V5.0 Arsenal)

We threw browser tabs out the window. V5.0 combines a custom FastAPI backend with a PyWebView native shell to achieve zero-latency interactions, cinematic visual effects, and a pure software experience.

- 🖥️ **Native Desktop Shell (NEW in V5.0):** No more terminal black boxes. No more local host URLs. Helix is now a compiled `.exe` with a transparent taskbar icon and a borderless UI. Double-click to boot the entire AI engine silently in the background.
    
- 🌧️ **Matrix Decryption Engine:** A custom HTML5 Canvas rendering engine. When the AI thinks, your screen rains digital matrix code. Features a "Smart Braking System" that seamlessly fades the animation the exact millisecond your data arrives.
    
- 🧠 **SYNAPSE Core (The Copilot):** A built-in, GLM-powered conversational agent. **Mount Intel** from your local Vault and ask the engine to analyze code, summarize papers, or evaluate commercial value in real-time. Features bulletproof null-state handling.
    
- 🗂️ **The Secure Vault:** A local intelligence library. Access all historical reports instantly within the app. Features dynamic filtering (`ALL | ARXIV | GITHUB`), explosive GSAP `clip-path` transitions, and in-app Markdown decryption.
    
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

**1. The AI Brain Key (GLM-4):**

- Go to **[open.bigmodel.cn](https://open.bigmodel.cn/)** (Zhipu AI) and register for a free account.
    
- Click on your profile/dashboard and find the **"API Keys"** menu.
    
- Click "Create new API key" (or copy the default one). It will look like a long string of random letters and numbers. Keep this page open.
    

**2. The Email Dispatch Key (163 Mail):**

- _Note: Helix uses 163.com by default, but you can use others if you know how to configure SMTP._
    
- Log into your 163 email account on the web.
    
- Go to **Settings** -> **POP3/SMTP/IMAP**.
    
- Turn **ON** the "SMTP Service".
    
- It will ask you to verify your phone number and will then give you an **Authorization Code**. It usually looks like a 16-letter random password.
    
- 🚨 _Never use your actual email login password! Only use this special Authorization Code._
    

### Phase 4: Configure The Secret File (`.env`)

Now we need to put your keys into the Helix control panel.

1. In your extracted Helix folder, find the file named `.env.example`.
    
2. Right-click it, select **Rename**, and delete the `.example` part. It should now be named EXACTLY: `.env` _(Troubleshooting: If your computer hides file extensions and names it `.env.txt`, you need to go to View -> Show -> "File name extensions" in your Windows folder and fix it)._
    
3. Right-click your new `.env` file and select **"Open with" -> Notepad**.
    
4. Fill in the blanks with the keys you just got. It should look like this:
    
    Plaintext
    
    ```
    GLM_API_KEY="paste_your_long_zhipu_api_key_here"
    OBSIDIAN_PATH="C:/Users/YourName/Desktop/Helix_Vault"
    
    SENDER_EMAIL="your_email@163.com"
    EMAIL_PASSWORD="paste_your_16-letter_authorization_code_here"
    RECEIVER_EMAIL="where_you_want_to_receive_reports@gmail.com"
    ```
    
5. Save the file and close Notepad.
    

### Phase 5: Assembly (Opening the Terminal)

We need to download a few extra parts (libraries) to make the code run and build your app.

1. Open your Helix folder (where `api.py` and your new `.env` file are).
    
2. Click directly on the **folder address bar** at the top of the window (where it says something like `C:\Users\Desktop\Helix`).
    
3. Delete all the text in the bar, type the letters **`cmd`**, and press **Enter**.
    
4. A black hacker-looking window (the Terminal) will pop up. Don't panic!
    
5. Copy and paste the exact text below into the black window and press **Enter**:
    
    Bash
    
    ```
    pip install -r requirements.txt
    ```
    
6. You will see a lot of text scrolling by. Wait for it to stop and say "Successfully installed...". This means your engine is ready.
    

### Phase 6: Forging the Desktop App (One-Time Setup)

We are going to turn this code into a real Windows application so you never have to look at a black terminal again.

1. Still in that black `cmd` window from Phase 5, copy and paste this ultimate command and press **Enter**:
    
    Bash
    
    ```
    pyinstaller --name "Project_Helix" --noconsole --onefile --icon=icon.ico HelixApp.py
    ```
    
2. The matrix will start scrolling rapidly. This is normal! It is building your app. Wait 1-3 minutes until it says `completed successfully`.
    
3. You can now close the black terminal window forever.
    

### Phase 7: The Elegant Setup (Desktop Shortcut)

Now, let's put it on your desktop like a professional app.

1. Look inside your Helix folder. You will see a newly created folder called **`dist`**. Open it.
    
2. Inside, you will find your shiny new application: **`Project_Helix.exe`**.
    
3. 🚨 **CRITICAL STEP:** Right-click `Project_Helix.exe` and select **Cut**. Go _back_ to your main Helix folder (where `index.html` and `.env` live) and **Paste** it there. _(It must live in the exact same room as your secret keys!)_
    
4. Right-click your newly pasted `Project_Helix.exe`, hover over **"Send to"**, and click **"Desktop (create shortcut)"**.
    
5. Go to your computer's Desktop. Find the new shortcut, right-click it, select **Rename**, and call it something cool like `Helix Command Center`.
    

### 🚀 IGNITION! (Your Daily Routine)

You are done. You only had to do Phases 1-7 once. You never have to touch code again.

Whenever you want to use Helix, simply **double-click the `Helix Command Center` shortcut on your desktop**. A beautiful, borderless Matrix window will open instantly. Click **IGNITE**, sit back, and watch the magic happen!

---

## ☁️ Cloud Autopilot & Ghost Sync (The Hybrid Arch)

Helix isn't just a local app; it's a **True Hybrid System**. Configure `.github/workflows/daily_hunt.yml` and `githuber.yml` with your repository secrets. GitHub's enterprise Linux servers will autonomously hunt at 6:17 AM and 10:29 AM every day, bypassing local network restrictions. **V5.0 Update:** The cloud bypasses strict `.gitignore` rules to force-sync Markdown reports into your repository. Whenever you open your local Helix App, it automatically fetches these cloud reports straight into your local Vault. You wake up, and the intel is already there.

---

## 🗺️ Roadmap

- [x] **V2.0:** Base LLM integration, SMTP setup, and daily automation via Actions.
    
- [x] **V3.5:** Velocity Radar, CTO Persona, Smart Folder Routing.
    
- [x] **V3.6.0 (The UI Overhaul):** Complete front-end/back-end separation (FastAPI + JS). Implementation of **SYNAPSE Copilot**, GSAP Animations, Local Vault Reader, and State Memory.
    
- [x] **V4.0.0 (The Matrix Edition):** Cinematic data-driven code rain, intelligent UI braking system, robust `.env` vs UI payload routing, and foolproof empty-state handling.
    
- [x] **V5.0.0 (The Desktop Singularity):** Transformed the SPA into a standalone Windows `.exe` application using PyWebView and PyInstaller. Eliminated terminal requirements, solved transparent icon caching, and implemented the foolproof setup guide.
    
- [ ] **V5.1.0 (Cross-Platform Expansion):** Adapt the PyWebView compilation pipeline for native macOS (`.app`) and Linux (`.AppImage`) support.
    
- [ ] **V6.0.0 (Local LLM Integration):** Decouple from cloud API keys. Implement seamless hookups for local open-source models (e.g., Ollama, Llama-3) for absolute, air-gapped data privacy.
---
*Built with excessive amounts of coffee, minus sleep, and a refusal to read bad papers manually.*