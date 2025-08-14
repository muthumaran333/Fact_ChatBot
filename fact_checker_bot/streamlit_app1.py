# streamlit_app1.py
import streamlit as st
from src.agent_wrapper import get_agent

# ================== Page Config ==================
st.set_page_config(page_title="FactChecker Bot", layout="wide")

# ================== Image URLs ==================
LOGO_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Magnifying_glass_icon.svg/1024px-Magnifying_glass_icon.svg.png"
USER_AVATAR = "https://i.ibb.co/N3ZVZrG/user-avatar.png"
BOT_AVATAR = "https://i.ibb.co/4YwK5z0/bot-avatar.png"

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
    st.image(LOGO_URL, width=120)
    st.markdown("### Instructions:")
    st.markdown(
        "1. Enter a claim or question.\n"
        "2. Optionally upload a file/image.\n"
        "3. Press **Send** to check facts."
    )

# ================== Initialize Agent ==================
agent = get_agent()

# ================== Chat Display (history first) ==================
for message in st.session_state.chat_history:
    # Bot's message - left aligned
    if message["bot"]:
        st.markdown(
            f"""
            <div style='display: flex; align-items: flex-start; margin-bottom: 12px;'>
                <img src="{BOT_AVATAR}" width="40" style="border-radius:50%; margin-right:10px;">
                <div style='background: linear-gradient(145deg, #EDEDED, #F9F9F9); color: #333;
                            padding: 12px 18px; border-radius: 12px; max-width: 70%;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                    {message['bot']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # User's message - right aligned
    if message["user"]:
        st.markdown(
            f"""
            <div style='display: flex; justify-content: flex-end; align-items: flex-start; margin-bottom: 12px;'>
                <div style='background: linear-gradient(145deg, #4facfe, #00f2fe); color: white;
                            padding: 12px 18px; border-radius: 12px; max-width: 70%;
                            box-shadow: 0 3px 7px rgba(0,0,0,0.3); margin-right:10px;'>
                    {message['user']}
                </div>
                <img src="{USER_AVATAR}" width="40" style="border-radius:50%; margin-left:10px;">
            </div>
            """,
            unsafe_allow_html=True
        )

# ================== File Upload & Input (BOTTOM) ==================
uploaded_file = st.file_uploader(
    "Upload a file or image (optional)",
    type=["txt", "pdf", "png", "jpg", "jpeg"]
)

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your claim here...")
    submitted = st.form_submit_button("Send")

    if submitted and user_input.strip():
        with st.spinner("Fact-checking..."):
            # Handle uploaded file (placeholders)
            if uploaded_file:
                if uploaded_file.type.startswith("image/"):
                    st.warning("OCR processing not yet implemented.")
                elif uploaded_file.type in ["text/plain", "application/pdf"]:
                    st.warning("Text extraction not yet implemented.")

            # Get bot response
            bot_response = agent.check_claim(user_input)

        # Save to history
        st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
        st.experimental_rerun()
