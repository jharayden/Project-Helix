# 🧬 Project Helix: The Autonomous AI Intelligence Suite

![Version](https://img.shields.io/badge/Version-3.5.0-blue.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg?style=for-the-badge)
![Brain](https://img.shields.io/badge/Brain-GLM--5-purple.svg?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Cloud-GitHub_Actions-2088FF.svg?style=for-the-badge&logo=github)

Welcome to **Project Helix**. This is no longer just a paper reader; it is a **Dual-Strand Autonomous Microservice System** designed to extract pure signal from the noise of both academic research and open-source engineering. 

It runs entirely on GitHub Actions (Zero server costs) and dispatches highly readable, CTO-level briefings directly to your Email and Obsidian Vault.

- 🌅 **Strand A (The Morning Track - `hunter.py`):** Scans the Arxiv database for the latest papers. The "Geek Professor" agent evaluates them and delivers the Top 3 theoretical breakthroughs.
- 🌃 **Strand B (The Nightly Track - `githuber.py`):** Scans the GitHub API for the fastest-growing AI repositories. The "Silicon Valley CTO" agent evaluates the commercial value and developer friction of the Top 1 "Lobster" (killer app).

Stop scrolling through abstract feeds. Let Helix hunt the signal for you.

---

## 🚀 The Core DNA (V3.5 Arsenal)

- **🧠 Dual Cognitive Engines (GLM-5):**
  - *The Professor (Arxiv):* Evaluates academic novelty and methodology.
  - *The CTO (GitHub):* Answers the "Soul Questions" - What is it? What's the commercial value? How hard is it to deploy? What's the ideal workflow?
- **📡 The Velocity Engine (GitHub Radar):** Bypasses static "Total Stars" metrics. Calculates the real-time growth velocity (`Stars / Hours Alive`) to capture exploding repositories before they hit the mainstream.
- **🗂️ Smart Storage Routing:** Automatically creates `Arxiv_Papers` and `GitHuber` subfolders inside your Obsidian Vault. Implements collision-free file naming (`Catch_YYYY-MM-DD_N.md`).
- **📨 Regex Text Slicer:** Automatically strips heavy Obsidian Callout syntax (`> [!info]`) in memory, translating the payload into a beautifully clean, plain-text email for mobile reading.
- **🛡️ Bulletproof Execution:** Hardcoded proxy bypasses (`NO_PROXY="*"`) for Windows environments, and SMTP hostname masking (`localhost`) to prevent GBK/UTF-8 decoding crashes on local machines.

---

## 🛠️ Installation & Deployment (Foolproof Guide)

### Step 1: Clone & Install Dependencies
Get the code onto your local machine:
```bash
git clone [https://github.com/yourusername/project-helix.git](https://github.com/yourusername/project-helix.git)
cd project-helix
pip install arxiv openai python-dotenv requests
```

### Step 2: Configure the Vault (The `.env` File)
Create a `.env` file in the root directory. This is your vault for API keys. **Never commit this file to public repositories.**

```env
# Cognitive Engine
GLM_API_KEY="your_zhipu_glm_api_key_here"

# Storage Routing (Use absolute paths)
OBSIDIAN_PATH="D:/obsidian/vault/PROJECT_HELIX" 

# Email Dispatch
SENDER_EMAIL="your_bot_email@163.com"
EMAIL_PASSWORD="your_smtp_app_password" # Use App Password, NOT your real password
RECEIVER_EMAIL="your_personal_email@gmail.com"

# Strand A: Arxiv Targeting
TARGET_TOPIC="Embodied AI"

# Strand B: GitHub Radar (Optional, prevents API rate limiting)
GITHUB_TOKEN="your_classic_github_personal_access_token"
```

### Step 3: Local Ignition (Testing)
Before going to the cloud, test both engines locally. The scripts will automatically create subfolders in your Obsidian path and fire off emails.

```bash
# Run Strand A (Morning Paper Agent)
python hunter.py

# Run Strand B (Nightly GitHub Agent)
python githuber.py
```

### Step 4: Cloud Autopilot (GitHub Actions)
To make this run automatically every day for free:
1. Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Add all the keys from your `.env` file as **Repository Secrets** (e.g., `GLM_API_KEY`, `SENDER_EMAIL`, etc.).
3. The agents are scheduled via `.github/workflows/daily_hunt.yml` and `.github/workflows/githuber.yml`. They are pre-configured to run at off-peak hours to avoid GitHub's server queues. You can adjust the `cron` timings inside those files if needed.

---

## 🗺️ Roadmap

- [x] **V2.0:** Base LLM integration, SMTP setup, and daily automation via Actions.
- [x] **V3.1.6:** Professor Persona, Regex Email Slicer, Collision-Free Storage.
- [x] **V3.5.0:** **Project Helix (Dual-Strand Microservices)**, Velocity Radar, CTO Persona, Smart Folder Routing.
- [ ] **V3.6 (Upcoming):** `Better UI` - Enhancing the design and user experience of the local Streamlit Web UI.
- [ ] **V4.0 (The Vision):** Complete front-end/back-end separation. FastAPI driven backend with a fully interactive, WebGL-powered 3D Dashboard driven by AI state.

---
*Built with excessive amounts of coffee, zero sleep, and a refusal to read bad papers manually.*