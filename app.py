import streamlit as st
import os
from dotenv import load_dotenv
from hunter import ArxivHunter # 直接把你写的引擎导入进来！

# ==========================================
# 1. 注入灵魂：极简暗黑风 CSS 装甲
# ==========================================
st.set_page_config(page_title="Arxiv Hunter V2.0", page_icon="🏎️", layout="centered")

custom_css = """
<style>
    /* 隐藏 Streamlit 默认的顶部菜单和底部水印 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 定义全局字体和极致暗黑背景 */
    html, body, [class*="css"]  {
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    
    /* 让按钮看起来像跑车的点火开关 */
    div.stButton > button:first-child {
        background-color: #00FF66; /* 荧光绿 */
        color: #000000;
        font-weight: 800;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s ease-in-out;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #00CC52;
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(0, 255, 102, 0.4);
    }
    
    /* 输入框的极简处理 */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #333;
        background-color: #111;
        color: #00FF66;
        font-weight: bold;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 2. 驾驶舱 UI 布局
# ==========================================
st.title("🏎️ Arxiv Hunter _V2.0_")
st.caption("Autonomous Academic Telemetry Dashboard")
st.markdown("---")

# 接收你的动态指令
query = st.text_input("🎯 Enter Target Sector (e.g., Embodied AI, Large Language Models):", value="Embodied AI")

# 点火按钮
if st.button("IGNITION (Start Hunt)"):
    if not query:
        st.warning("Please enter a target sector!")
    else:
        # ==========================================
        # 3. 唤醒你的 V8 后端引擎
        # ==========================================
        with st.spinner(f"🚀 Telemetry online. Hunting top papers in '{query}'... (This may take 30-60 seconds for Deep Thinking)"):
            try:
                # 读取保险箱
                load_dotenv()
                api_key = os.getenv("GLM_API_KEY")
                obsidian_path = os.getenv("OBSIDIAN_PATH")
                sender_email = os.getenv("SENDER_EMAIL")
                app_password = os.getenv("EMAIL_PASSWORD")
                receiver_email = os.getenv("RECEIVER_EMAIL")
                
                # 实例化引擎
                hunter = ArxivHunter(glm_api_key=api_key)
                
                # Phase 2: Hunt
                papers = hunter.hunt_papers(query=query, max_results=15)
                
                # Phase 3: Digest
                report = hunter.digest_papers(papers=papers)
                
                # Phase 4: Report (保存并发送)
                if not report.startswith("> [!error]"):
                    hunter.save_report(content=report, vault_path=obsidian_path)
                    hunter.dispatch_email(
                        content=report, 
                        sender_email=sender_email, 
                        app_password=app_password, 
                        receiver_email=receiver_email, 
                        smtp_server="smtp.163.com"
                    )
                    st.success("🏁 Mission Accomplished! Check your Obsidian & Email.")
                    
                    # 在网页上直接把结果渲染出来给你看！
                    st.markdown("### 📊 Live Telemetry Feed:")
# 视觉滤镜：把 Obsidian 独有的色块代码替换成 emoji 标题，让网页渲染更优雅
                    ui_report = report.replace("[!info]", "💡").replace("[!summary]", "⚙️").replace("[!example]", "🚀")
                    st.markdown(ui_report)
                else:
                    st.error("Engine Misfire in Cognitive Layer.")
                    
            except Exception as e:
                st.error(f"System Crash: {e}")