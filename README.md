# 🎯 Arxiv Hunter: The Autonomous AI Research Agent

![Version](https://img.shields.io/badge/Version-3.1.6-blue.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg?style=for-the-badge)
![Brain](https://img.shields.io/badge/Brain-GLM--5-purple.svg?style=for-the-badge)
![Deployment](https://img.shields.io/badge/Cloud-GitHub_Actions-2088FF.svg?style=for-the-badge&logo=github)

**Arxiv Hunter** is a highly opinionated, autonomous intelligence agent designed to solve the "academic noise" problem. It wakes up every day at an off-peak custom time via CRON (e.g., 6:17 AM Beijing Time), scans the Arxiv database for the latest papers in your specific field (e.g., Embodied AI), uses the **GLM-5** cognitive engine to deeply evaluate them, and dispatches a highly readable, "Geek Professor" style report directly to your **Email** and **Obsidian Vault** before you even brew your morning coffee.

Stop scrolling through abstract feeds. Let the Agent hunt the signal for you.

---

## 🚀 Key Features (V3.1.6 Arsenal)

- **🧠 Full-Depth Cognitive Engine (GLM-5):** Adopts a "Professor/Bro" persona—technical expertise meets friendly peer. Utilizing strict **Anti-Laziness Prompt Engineering**, it guarantees exactly Top 3 papers per run, ensuring non-truncated, substantial analysis (2-3 thick paragraphs per section) for *every* selected paper.
- **🛡️ Hardcoded Proxy Bypass:** Executes `os.environ["NO_PROXY"] = "*"` at launch. This completely blinds Python to underlying system/registry proxy configurations (crucial for Windows hosts), ensuring bulletproof API request stability.
- **📡 Dual-Dispatch Slicer (Regex-Powered):**
  - **Vault Mode:** Outputs raw, beautifully formatted Obsidian Markdown utilizing custom Callouts (`> [!info] 🎯 Target Locked`) and dynamic, content-aware `#Tags`.
  - **Email Mode:** Features a bulletproof Regex Text Slicer V3.1.5 that translates complex Obsidian syntax into clean, readable plain text on the fly. It now dispatches the **FULL** content of all three papers (including full Professor's Deep Dives) to your inbox with no truncation.
- **🗂️ Collision-Free Storage System:** Implements an auto-incrementing local file storage logic (`Arxiv_Hunter_YYYY-MM-DD_N.md`). No matter how many times you trigger the agent per day via web or terminal, historical data is never overwritten.

---

## ⚙️ Architecture Workflow

1. **[SENSORS] Target Acquisition:** Queries Arxiv API based on the dynamic `TARGET_TOPIC`. Extracts Title, Authors, Abstract, and direct entries IDs for Zotero integration.
2. **[COGNITIVE] Deep Evaluation:** Sends the payload to GLM-5. The model executes Top 3 selection based on strict structural and impact constraints, maintaining extreme technical depth.
3. **[STORAGE] Vault Write:** Performs collision detection on the local file system and saves the raw Obsidian Markdown via auto-incrementing filenames.
4. **[DISPATCH] Email Translation:** The Regex engine sanitizes the text, updates the email subject dynamically based on the paper's tags, and transmits full intelligence via SMTP.

---

## 🛠️ Quick Start (Deploy Your Own Hunter)

### 1. Local Environment Setup
Clone the repo and install the minimal dependencies:
```bash
git clone [https://github.com/yourusername/arxiv-hunter.git](https://github.com/yourusername/arxiv-hunter.git)
cd arxiv-hunter
pip install arxiv openai python-dotenv
```

### 2. Configure the Vault (Secrets)
Create a `.env` file in the root directory and add your credentials:
```env
GLM_API_KEY="your_zhipu_api_key_here"
OBSIDIAN_PATH="C:/Users/YourName/Documents/Obsidian Vault/AI_Research"
SENDER_EMAIL="your_bot_email@163.com"
EMAIL_PASSWORD="your_smtp_app_password"
RECEIVER_EMAIL="your_personal_email@gmail.com"
TARGET_TOPIC="Embodied AI" # Default fallback
```

### 3. Configure the Autopilot (CRON)
Open `.github/workflows/daily_hunt.yml` and set your preferred off-peak hunting time. **Pro Tip:** Avoid exact hours like `0 0 * * *` to bypass GitHub Actions traffic jams. Use offset times like `17 22 * * *`.

### 4. Ignite the Engine
Run the agent manually to test the full pipeline:
```bash
python hunter.py
```

---

## 🗺️ Roadmap

- [x] **V2.0:** Base LLM integration, SMTP setup, and daily automation via Actions.
- [x] **V3.1.6:** Professor Persona, Bulletproof Regex Email Slicer (full text), Zero-Overwrite Storage, Zotero link extraction, Proxy Bypass.
- [ ] **V3.5 (Upcoming):** `GitHub Trend Hunter` - Expanding sensors to scrape and deeply evaluate daily trending open-source AI repositories.
- [ ] **V3.5.1 (Upcoming):** `Better UI` - Enhancing the design and user experience of the Web UI, expand the ability of the Web UI, adding cool animation effects.
- [ ] **V4.0 (The Vision):** Complete front-end/back-end separation. FastAPI driven backend with a fully interactive, WebGL-powered 3D Dashboard driven by AI state.

---
*Built with excessive amounts of coffee and a refusal to read bad papers manually.*