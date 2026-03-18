# 🏎️ Arxiv Hunter V2.0: Autonomous Academic Telemetry

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An autonomous AI agent and local telemetry dashboard designed to hunt, digest, and dispatch the latest Arxiv papers (e.g., Embodied AI, LLMs). Built from first principles, it leverages Large Language Models (GLM-5) to filter the noise and deliver high-signal, deep-tech summaries directly to your inbox and Obsidian vault.

## ✨ V2.0 Core Upgrades
- 🎛️ **Telemetry Dashboard:** A sleek, dark-mode Streamlit Web UI for real-time local operation and dynamic topic switching.
- 🧠 **Deep Cognition Engine:** Automatically scans 15+ papers, evaluates structural novelty, and ranks the **Top 3**.
- 🔗 **Zotero Ready:** Hardcodes direct Arxiv PDF URLs into the output for seamless citation management.
- ☁️ **Cloud Autopilot:** Pre-configured GitHub Actions YAML for zero-touch, daily 8:00 AM automated email dispatches.

---

## 🛠️ Quick Start Guide

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/arxiv-hunter.git](https://github.com/your-username/arxiv-hunter.git)
cd arxiv-hunter
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
pip install streamlit  # Required for the local Web UI
```

### 3. Configure the Engine (Crucial Step!)
This project strictly isolates credentials. You must set up your local environment variables:
1. Find the file named `.env.example` in the root directory.
2. Copy it and rename the new file to exactly `.env`.
3. Open `.env` and replace the placeholder text with your actual API keys and email credentials.

### 4. Ignite the Dashboard (Local Mode)
To launch the interactive control panel on your local machine, run:
```bash
streamlit run app.py
```
A new browser tab will open. Enter your target sector and hit **IGNITION**!

---

## ☁️ Autopilot Deployment (GitHub Actions)
Want to wake up to a fresh intelligence report every morning?
1. Fork this repository.
2. Go to your repository **Settings > Secrets and variables > Actions**.
3. Add your secrets (`GLM_API_KEY`, `SENDER_EMAIL`, `EMAIL_PASSWORD`, `RECEIVER_EMAIL`) matching the exact names in the `.env` file.
4. Enable the workflow in the **Actions** tab. The agent will now run automatically every day at 16:00 UTC.

---
*Built with ☕, late-night calculus, and a passion for automation.*
