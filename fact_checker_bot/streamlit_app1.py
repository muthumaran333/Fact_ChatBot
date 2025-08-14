import os
import re
import streamlit as st
from src.agent_wrapper import get_agent
from google.generativeai import configure, GenerativeModel

# ================== Page Config ==================
st.set_page_config(page_title="FactChecker Bot", layout="wide")

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
if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

# ================== Sidebar ==================
with st.sidebar:
    st.image(LOGO_URL, width=120)
    st.markdown("### 📝 Sample Claims to Try:")
    for claim in [
        "Delhi is the capital of India.",
        "The moon is made of cheese.",
        "Water boils at 100°C at sea level.",
        "Mount Everest is the tallest mountain in the world.",
        "Sharks are mammals.",
        "The Great Wall of China is visible from space.",
        "Bananas grow on trees.",
        "The Pacific Ocean is the largest ocean on Earth.",
        "Humans have walked on Mars.",
        "Lightning never strikes the same place twice."
    ]:
        st.markdown(f"- {claim}")

# ================== Gemini Initialization ==================
API_KEY = os.getenv("GOOGLE_API_KEY", "your_api_key_here")
configure(api_key=API_KEY)
gemini_model = GenerativeModel("gemini-2.5-flash")

def clean_output(text: str) -> str:
    """Remove markdown formatting like **, *, etc."""
    return re.sub(r"(\*\*|\*)", "", text)

def fact_check_claim_with_gemini(claim: str) -> str:
    prompt = f"""
    You are a fact-checking assistant. Verify the following claim and respond in the format:
    Verdict: True/False/Partially True
    Explanation: Short factual reasoning with sources if possible.

    Claim: "{claim}"
    """
    try:
        response = gemini_model.generate_content(prompt)
        return clean_output(response.text.strip())
    except Exception as e:
        return f"Error: Gemini check failed: {e}"

# ================== Agent ==================
agent = get_agent()

# ================== Chat Messages ==================
for message in st.session_state.chat_history:
    if message["bot"]:
        st.markdown(
            f"""
            <div style='display: flex; align-items: flex-start; margin-bottom: 12px;'>
                <img src="{BOT_AVATAR}" width="40" style="border-radius:50%; margin-right:10px;">
                <div style='background: #f4f4f4; color: black; padding: 12px 18px; border-radius: 12px; max-width: 70%;'>
                    {message['bot']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if message["user"]:
        st.markdown(
            f"""
            <div style='display: flex; justify-content: flex-end; margin-bottom: 12px;'>
                <div style='background: linear-gradient(145deg, #e0e0e0, #f5f5f5); color: black;
                            padding: 12px 18px; border-radius: 12px; max-width: 70%;'>
                    {message['user']}
                </div>
                <img src="{USER_AVATAR}" width="40" style="border-radius:50%; margin-left:10px;">
            </div>
            """,
            unsafe_allow_html=True
        )

# ================== Bottom Chat Bar ==================
st.markdown("---")
col1, col2, col3 = st.columns([0.1, 0.75, 0.15])

with col1:
    if st.button("📎", help="Attach file"):
        st.session_state.show_uploader = not st.session_state.show_uploader

with col2:
    user_input = st.text_input(
        "Enter your claim...",
        placeholder="Type your claim here...",
        label_visibility="collapsed"
    )

with col3:
    send_clicked = st.button("➤", help="Send")  # Changed icon here

# File uploader appears only if toggled
uploaded_file = None
if st.session_state.show_uploader:
    uploaded_file = st.file_uploader(
        "Upload a file or image",
        type=["txt", "pdf", "png", "jpg", "jpeg"],
        label_visibility="collapsed"
    )

# Handle send click
if send_clicked and user_input.strip():
    with st.spinner("Fact-checking..."):
        if uploaded_file:
            st.warning("File processing not yet implemented.")
        bot_response = fact_check_claim_with_gemini(user_input)
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
    st.rerun()
