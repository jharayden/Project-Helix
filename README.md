# 🧬 Project Helix: The Autonomous AI Intelligence Suite

![Version](https://img.shields.io/badge/Version-3.6.0-00FF66.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688.svg?style=for-the-badge&logo=fastapi)
![Frontend](https://img.shields.io/badge/Frontend-Tailwind_|_GSAP-38B2AC.svg?style=for-the-badge)
![Brain](https://img.shields.io/badge/Brain-GLM--5-purple.svg?style=for-the-badge)

Welcome to **Project Helix v3.6: The Command Center**. 

We didn't just update the UI; we fundamentally rewrote the architecture. Project Helix has evolved from a headless background script into a **Decoupled, High-Octane Single Page Application (SPA)**. It is your private, cyberpunk-styled intelligence dashboard designed to extract pure signal from the noise of academic research and open-source engineering.

Stop scrolling through abstract feeds. Ignite the engine, and let Helix hunt for you.

---

## 🚀 The Core DNA (V3.6 Arsenal)

We threw Streamlit out the window and built a custom FastAPI + HTML/JS stack to achieve zero-latency interactions and cinematic GSAP animations.

- 🧠 **SYNAPSE Core (The Copilot):** A built-in, GLM-5 powered conversational agent. You can now directly chat with the Helix AI. **Mount Intel** from your local Vault and ask the engine to analyze code, summarize papers, or evaluate commercial value in real-time.
- 🗂️ **The Secure Vault:** A local intelligence library. Access all historical reports instantly within the browser. Features dynamic filtering (`ALL | ARXIV | GITHUB`), explosive GSAP `clip-path` transitions, and in-browser Markdown decryption.
- 🌅 **ARXIV Radar:** Scans the Arxiv database for the latest papers. The "Geek Professor" agent evaluates them and delivers the Top 3 theoretical breakthroughs. Now supports targeted sector searches (e.g., "Embodied AI").
- 🌃 **GITHUB Catch:** Scans the GitHub API for the fastest-growing AI repositories. Calculates real-time growth velocity (`Stars / Hours Alive`). Now supports targeted hunting or automatic fallback to global trending algorithms.
- ⚡ **Shared Memory Architecture:** Seamlessly switch between Arxiv, Github, and Synapse tabs. The UI features state preservation—your search inputs and terminal outputs remain exactly as you left them when navigating between strands.

---

## 🛠️ Installation & Deployment (Foolproof Guide)

### Step 1: Clone & Install Dependencies
Get the code onto your local machine:
```bash
git clone [https://github.com/yourusername/project-helix.git](https://github.com/yourusername/project-helix.git)
cd project-helix
pip install fastapi uvicorn openai arxiv python-dotenv requests
```

### Step 2: Configure the Vault (The `.env` File)
Create a `.env` file in the root directory. This is your vault for API keys. **Never commit this file to public repositories.**

```env
# Cognitive Engine
GLM_API_KEY="your_zhipu_glm_api_key_here"

# Storage Routing (Use absolute paths for local Vault synchronization)
OBSIDIAN_PATH="D:/obsidian/vault/PROJECT_HELIX" 

# GitHub Radar (Optional, prevents API rate limiting)
GITHUB_TOKEN="your_classic_github_personal_access_token"
```

### Step 3: Ignition (Local Command Center)
Helix v3.6 utilizes a true frontend-backend separation.

1. **Ignite the Backend API:**
   Open your terminal and start the FastAPI engine:
   ```bash
   python api.py
   # Or run via uvicorn directly: uvicorn api:app --reload
   ```
2. **Launch the Dashboard:**
   Simply double-click `index.html` in your browser. Welcome to the Command Center.

### Step 4: Cloud Autopilot (GitHub Actions - Legacy Support)
Helix still supports fully autonomous nightly dispatching via GitHub Actions.
Configure `.github/workflows/daily_hunt.yml` with your repository secrets to receive CTO-level briefings directly to your Email.

---

## 🗺️ Roadmap

- [x] **V2.0:** Base LLM integration, SMTP setup, and daily automation via Actions.
- [x] **V3.5.0:** Velocity Radar, CTO Persona, Smart Folder Routing.
- [x] **V3.6.0 (The UI Overhaul):** Complete front-end/back-end separation (FastAPI + JS). Implementation of **SYNAPSE Copilot**, GSAP Animations, Local Vault Reader, and State Memory.
- [ ] **V4.0 (Upcoming):** The Parallax Hero Section. A cinematic, WebGL-powered 3D landing sequence before dropping into the Command Center.
- [ ] **V4.5 (The Vision):** Create .bat/.command script to quick start. Use Tauri+React/Vue to design front end and transform FastAPI to a microservice， which might also include WebGL animation.
- [ ] **V5.0 (Tiny Upgration):** Language setting would be added.
- [ ] **V6.0 (The Vision):** Make it a real application in Windows/Mac system.

---
*Built with excessive amounts of coffee, zero sleep, and a refusal to read bad papers manually.*