# 🚀 Arxiv Hunter v1.0
**An Autonomous AI Agent for Academic Paper Hunting and Digestion.**

## 📌 What is this?
Arxiv Hunter is a fully automated, locally deployed Python agent. It scans the Arxiv database for the latest papers (currently focused on Embodied AI), uses Large Language Models (GLM-5) to analyze their structural novelty, and automatically dispatches the intelligence.

This is a **First Principles** implementation of an AI Agent, cleanly separating the Action Layer (Data Retrieval), Cognitive Layer (LLM Digestion), and Report Layer (File System & SMTP).

## ✨ Features (v1.0)
- **📡 Deterministic Telemetry:** Automatically queries Arxiv API for the latest submissions.
- **🧠 Cognitive Digestion:** Uses Zhipu GLM-5 (with Deep Thinking enabled) to filter noise and select the most valuable paper.
- **📝 Obsidian Native Integration:** Writes the analysis directly to a local Obsidian Vault using native callouts (`> [!info]`) and `#tags`.
- **📧 Zero-Dependency Email Dispatch:** Slices the Markdown into a highly readable, clean summary and pushes it to the user's target email via native Python `smtplib`.
- **🔐 Enterprise-Grade Security:** Utilizes `.env` and `.gitignore` to strictly decouple API keys and passwords from the source code.

## 🗺️ Roadmap (V2.0 Coming Soon)
- [ ] **Web UI Control Panel:** Dynamic input for search queries (no more hardcoded topics).
- [ ] **Zotero Integration:** Inclusion of direct Arxiv PDF URLs.
- [ ] **Deep Dive Expansion:** Expanding the context window to evaluate Top 3 papers with richer technical depth.

---
*Built with coffee, calculus deadlines, and a passion for Embodied AI.*