# streamlit_app1.py
import streamlit as st
from pathlib import Path
from src.agent_wrapper import get_agent

# ================== Page Config ==================
st.set_page_config(page_title="FactChecker Bot", layout="wide")

# ================== Constants ==================
IMG_PATH = Path("assets") / "image.png"
IMG_URL = "https://www.bing.com/th/id/OIP.jO12HDqKTbrBYUQ6x5KyeAHaHa?w=209&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2"

USER_AVATAR = "https://www.bing.com/th/id/OIP.iTBKcTgKFeA0YBO48ghWLgHaHa?w=182&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2"
BOT_AVATAR = "data:image/webp;base64,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"

# ================== Title ==================
st.markdown(
    "<h2 style='text-align: center; color: #333;'>🕵️ FactChecker Bot</h2>",
    unsafe_allow_html=True
)

# ================== Session State ==================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ================== Sidebar ==================
with st.sidebar:
    if IMG_PATH.is_file():
        st.image(str(IMG_PATH), width=120)
    else:
        st.image(IMG_URL, width=120)
    
    st.markdown("### Instructions:")
    st.markdown(
        "1. Enter a claim or question.\n"
        "2. Optionally upload a file/image.\n"
        "3. Press **Send** to check facts."
    )

# ================== Initialize Agent ==================
agent = get_agent()

# ================== File Upload ==================
uploaded_file = st.file_uploader(
    "Upload a file or image (optional)",
    type=["txt", "pdf", "png", "jpg", "jpeg"]
)

# ================== User Input Form ==================
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your claim here...")
    submitted = st.form_submit_button("Send")

    if submitted and user_input.strip():
        with st.spinner("Fact-checking..."):
            # Handle uploaded file
            if uploaded_file:
                if uploaded_file.type.startswith("image/"):
                    st.warning("OCR processing not yet implemented.")
                elif uploaded_file.type in ["text/plain", "application/pdf"]:
                    content = uploaded_file.read()
                    st.warning("Text extraction from file not yet implemented.")

            # Get bot response
            bot_response = agent.check_claim(user_input)

        # Save to history
        st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

# ================== Chat Display ==================
for message in st.session_state.chat_history:
    # User message (right-aligned)
    st.markdown(
        f"""
        <div style='display: flex; justify-content: flex-end; margin-bottom: 12px;'>
            <div style='background: linear-gradient(145deg, #4facfe, #00f2fe); color: white;
                        padding: 12px 18px; border-radius: 18px 18px 0px 18px;
                        max-width: 70%; box-shadow: 0 3px 7px rgba(0,0,0,0.3);'>
                {message['user']}
            </div>
            <img src='{USER_AVATAR}' width='40' style='margin-left:10px; border-radius:50%;'>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Bot message (left-aligned)
    st.markdown(
        f"""
        <div style='display: flex; justify-content: flex-start; margin-bottom: 12px;'>
            <img src='{BOT_AVATAR}' width='40' style='margin-right:10px; border-radius:50%;'>
            <div style='background: linear-gradient(145deg, #EDEDED, #F9F9F9); color: #333;
                        padding: 12px 18px; border-radius: 18px 18px 18px 0px;
                        max-width: 70%; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                {message['bot']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
