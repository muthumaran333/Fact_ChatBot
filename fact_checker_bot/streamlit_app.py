# # streamlit_app1.py
# import os
# import re
# import streamlit as st
# from src.agent_wrapper import get_agent
# from google.generativeai import configure, GenerativeModel

# # ================== Page Config ==================
# st.set_page_config(page_title="FactChecker Bot", layout="wide")
# LOGO_URL = "https://media.istockphoto.com/id/2178949438/vector/chatbot-icon-bot-sign-design-chatbot-logo-concept-robot-head-in-a-speech-bubble-online.jpg?s=612x612&w=0&k=20&c=_X5HzRHbp6PP6UIU2nsv86qxEJIpuwmqvEJ4V_pFnZc="
# USER_AVATAR = "data:image/webp;base64,UklGRj4OAABXRUJQVlA4IDIOAAAwVQCdASqHATIBPp1Oo0wlpKMiJfToiLATiWVu6B/IuzgEbhSsDT+Y+/42p7b+6c6P1l9Q4Yg83eblD9Tv6j3rPOmvpv6k/6fta/W7cHr39af8n6Bf5vvJ4AXh3eYwBfVj0fpl/1wwYniv8nyMfYHsK9L/0khsZE2E3I/G9VX5jh4ajhuf6pxAkvGkAAQCv/5S/j5HK7Ye9i75H1jtK3RkdmW/dHuD6BwNepISXgTAjwuWvnpBsMCmya4Jh8yLgNAeSI19a1bmVZsjLRaxRxGuqOQsp/MmjWmHA3vClURcUlrV01BwKwhfi75+3bwdDUp46yk5LWsumrdzxoPsVR/HjPthDDtvCp80bod3NiCmJlnwwubIG8DejKPlyNGwOA6MT2+xfKxGNC4A8ZvaxhhdDjgbgyHg9AAhCFTSqNH3sZi9nKhqRDtnDqsTtxikQvRoAI0yGjz0A3kqkYAT+Pr2FZvG9GSYlxqPsCdT7zzEfOcoDEPITotxMeozt+o1M/MG+GW+lPPHtZCDiDOux8bXyD/+xKpx0V2HIEBGrE75LOKMr6YFi7zeH+Ec6cnGirFxUEjEkzIZ+kFmCoe8jVieGoVKhE+0HTih75fC32sa+HSTC+XXbeSL95BgjkrfCcc8aCSdn2EZNd8cYuNfM2E+F/je/7wlAbEVTypV+DKEMrE8SAxeOMSs2qjAQH5aVyL/vXoUQJkLv7vzyUuqsTxFpbkGWxyH59aOC5gdoPmVxzJRvXHWWJW4y/+RMmxpXdqGPUV3y1Fg3U/dmmpOeZrHT7zDmvAoZV+7Zp69tOU3hINOPcfmfQWa46K6e5r0MM6ig/ZaeCCTPoOLpASuk0kNQoXcj77d5d3+NK7tQx7K5MpWjftRgOBrk0uqXjSuPDjr0KmnmkjNGb1mavS33ucpLUAA/vyrYf0sQWuQAA/HQZO6F0dAuDUFFc2w3NYlGM6OYza3cmJOhJycqdzUt3F5Q+JMp7NxegBdaoViaXt6b3kdseUilYzpbJ5UOVCSYtPE9uFKD829Dh3I52Mkj03CWNJmDCkMErsVen4y+a1gmx1XPZgQ39OWJqgkjMySX21Qe7aShfOJqydy+25Wg2A4nEjxxERIU0/igAi2pNVPEj2itmjL4vet1fUX8bMHl8sSsUNxpVgeFdcqy6rG0Ly8A1udPpSANns8/G2vQLkJYc66VLtvVZA7YWN0FD9TDxnfWLnQOo2vHRQKUSfqCUZ7MWj65Zube4FI926xQ+dhMAE2NcY5tDunPBJfCglVotY8vb51Upf4FpeYuUj4MGkwt7EvG4Al5m9URYRIH9+hTeTlxG1IOL2gL/SQ6UgYLhdBYA4HoyOlcNbRxQPwBH4lDAl9OxXngCoUGO4heALOkw7aAkAGtYWQeXmEUUAGwfK8zB8twcpGJ9v7osczV4TEha39l6sLk6B4pbcoTIpgwOU5NpHjao4MnVGi9jk8trC1XHKQNbqiZlDUnM0HtLOP4ACV9AxKTWHeJOmGC/HGBFa9aVRPUOC94WSJKY6FW8rwIqkm8aBj6jAL/SqHHJ12VNiO9LGvQ6/77ccHkdaST1dRIXWSjTl6v3ThUbyuK2BeA8lLzkJ4Fy7x8NDpGVpgMZqxz9t+BXfktrgLBHd5Rrx4THGsbQDraDZGAt8Buyj5TzKp341DbN5vKOOmTxmQX/XGNBxNFB9i84HcKKgRl22/Tdrqx1YL4TZnmZalu3w8Ov+vy85+/ZvFHnpga1CICh91VaFFCrsGdfi1miJvPuz4I968jt8GfZCTP8AzPF/PQu9LjpeyeolWwswPlJzjHq0FGqoIkDloXGKqorTPjGd0CusvF3U5v81Ig9DG08qq+vRkJjB9A2jGTq59DX3ZOWORNkCmpGiHL5TGXQQIWSP0gIvR1o93CpvBI7mVAxh/auVYrhLEp5gI4O9s693xzqh2JMc5Yea9QaeReFUy5c23B9/sBB9SDiTs/uftZFZ3K5MmWWRslBBffgsBD1z3UrYBT1y3lV+hTxaF+ywbjpVJawZuuNWKR0ya8l8wHwgOPJwNcTuAESyEnRl1XG6tvCGZ2Xt4Yilm6wa752iYdsOZ9Que1cHDYrU8jy6dTIS3gfgqzbTFe6gI/oeohbOPeuTMGGylsDVFnUPOKmhb2w3LO8tXPaULunqAJWOTK14QV4H4KaTAd+y4M3vtCj44RrQwhN6lvxzGs4Vxs0IV2VNxv0VjYH0ZKacvzPS4XaJ7rAZeEoeHZx2teZ59J2zRP7Upy/bLg6BXT6YWk+DMAsdvOnOGzwN5YJw1Ob0RuqRb3ARY+xou14OePgAWU3SMrRQV+GSUKvusvZI+E4dMERqOGU2V+SRNAyyzOG+odQZrBoYj/E5iUbsYiPubDNK7giHE4e/V8HHv1Gl5/Da4Nt2Uj6IXhr/MwLxnx9FVS99QnF1gd+CV9ow3Mn0vK5/pSakd7gGgKmCiwPJpQtap3pMC9rZQdvAzVpfzOGsa8tQf8K6G4G5P4Fh//HfTEXnZ/27RzCELZnBu6oux3MYh3KzXXIoBBGLZ4B1eoYfbURzjUkcsPHuQc8K9K/Rz84H2XNpxvUYZtDVVRwf5koDI2YyFkWGPmL5yPyQD0JyEFP0o46bMZjk/OzYzAHdQ00Inbjg8DliwBvcDLO+45VPp3G28Su+srVO2PGhE25xIwvO8pMus3LynnPR1jzPr+TprDnRlK+STvip5Wh4etkQh5WcFHa0SRCOEGqNT5NlVPYa0gR5PHT6rB34Kk62lysBc6uGwAeCB+RnQT6o/8gPsUhSI994+B51WDgUuj9UfawE8xSnHDILdsyJrOJoJsfPPNcBlcRx+AG4MdYPwSlAC+oZUza7yFK5Y9R/NLEwiD+xNcURFG1sJEsmRD5AvaUtokiUJd0fH6Hjxw2EReMDPCyqZ9RfCFLt0ILdFH0YmSX82FixmDOM4Eu+CDICzKJHKjC3wgXr2YncNeI8Iq02ZtQcEEoIq1CzFDJ8uTcJ5HE7pf6l15zbZUdbd8iW3yGAuFxe8n+BSqTLMCan7WQYCdFvUtXjVqgwFGX8BlbvKDXkUUZGuBMZXFsFucw6i0ytoz8tOdWSLkbji/dNk0vBD8Hlgfeo62DDv4a8v9HgivtQRwLxC0dhUHa5hxF2cHNvoCElocGLmeguE1jTp3yYALvmkMQUXrsfqgDhrrcx9TaMqPUh6T7wIcH/NGQ34bAucGijiLjQ3XwqbGbetbARGLoiaxlll27GEHUumHI1kGLeqG3lVScXkFg40S0inc1ZU/QFGKRcqtUvieLVqR2UqxoaXxIE5jUsDhp0OiobLZjBxG66mhlghfsudwCjhJfXXMruZcrU1j/7uU5A9r7wF9tmzkFpqRygVi6RuSALzWcODjBl15k/Hy7H5fRWx42TZmR/wzqCH0xSGMj/+kxHzjUEglV65KDzWrQTYjiNt+oD7ilGpvbP3wXSMLhO6D0mvhJWUwOlZNKE15ZniBLHgbOV+4z6md5MndmH9dvlgFozxX03yiBJKDZfwZRGCeols4eWRron36a0voYeOUg4XU/KUuqHL5hJfljwNDQQd7uZTUXzLwXzwmTdtLrAMSf51gKgzBYesAF00EYq7x4T0+C9ZLopu8TvvBgf1grVPqO0F3R2aA729h+BPI6QLBs+0Bn03Ngi/b/1e3TT8mf6xkFAgI3Z5yd9TFs7nri6bwqSN/EAk3osaAPu3vpOhXt4fhIANCq5Ht3G0YDM4MlwOAZjceJ2+7Ov412h2bxfm3VVQkpxX+pk9DovXaX/o7QA6Px3LNBtNelhh0CEUmrBY+t71yDrMAZ6efjTegmfzEyeg0ET+0kdcUzxsiYijh+2CGRMq5dr/zNa3UMU2R7pwVdFI+vsdDRjFDi3iwTdX4J/26VtRdeLp+3zhBO11xo7r9kgG8tUev8V9oAsRDnwvb6Jk5nyPwvaeLMJUZBDa66uV9z1WC+Jw4V+GhmD+j+WNFJuR0TzVsvH3bc9+hxdP7c1pxQyq4fPNr3WLb6+rRQXr8m3kGA3q+iHFvlQZTRUJgLuttTTp2llKcI/L2HEpDP4gsPZrUSr4zcwDujs8Hj66CHUBgyAzQeg8qPwEoPLEEnipyclA67Q254bdWLF+entKaWo2yO4N/VKnKwuRMjtTknDMoacG5xwmbXZZ3VU+nWVpTyANIT4rYFAUVCrQ9902q1eS38Qpvei1eN6/7Yhw0y57w3+Hhc2Sv9lsX7J/af9OePxWHz/ZcRjA3U9WzTLygNkyrUbHV1IPgoZVU48iajO8r6DhTqCRywjZ8BWH2VphlH2ZBL/l8YCdE/95QhMXkPYjVaeVYr7B+2j6iNbjMHIZI27YpuIyYmCV0rvy/wWTvQ5d9f/IAAWo8+awkgEVcs5+/kpMwa+wF4CUYdYL7f97Vwt45ucOUb6JYuEq20eSl6uklqsafp5WJvwNOAArmeiRQ3leFgJiYIFJkUSvT1j0WF0/NYraJAdRJUJVbd7agAAUhTEvV1J/dnaDmWbXSGwt4iuiLmaDs1mZ4VovP4unnrD1HP0lnlRakuB8f1VLz8P6d3X5ki20aFNVQ5xyjcYa2O9xRYPcUGPco24Ce3HY7SecawUUqWwA/C7DJ8XMUpzxCQxGfFTHePRmlxucP8sgh4DeaT7XOBmU8Ko5Ba0iRho/3pCIr+wFvBkRXR5uc+UbFMshHaK1SkOVCxczDg/ItJA8sgGopcjTn8m5GoH+nwl6qzd72Xx/PrC5FETaBKwcgjSQjf8KYZokC8jaSlf7ARa/DBkGkofLk7PsAAAAXlqGWhAFZ0QClfhEHruBzW2qzcfwIHAAAAI36QAA"
# BOT_AVATAR = "https://th.bing.com/th/id/OIP.3ffah5nxd1fBLy0g5xdKHQHaFs?w=274&h=211&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3"



# API_KEY = os.getenv("GOOGLE_API_KEY", "your_api_key_here")
# configure(api_key=API_KEY)
# gemini_model = GenerativeModel("gemini-2.5-flash")


# # ================== Gemini Initialization ==================

# def clean_text(text: str) -> str:
#     text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
#     text = re.sub(r"\*(.*?)\*", r"\1", text)
#     return text.strip()


# # ================== Fact-Checking Function ==================


# def fact_check_claim_with_gemini(claim: str) -> str:
#     prompt = f"""
#     You are a fact-checking assistant. Verify the following claim and respond in the format:
#     Verdict: True/False/Partially True
#     Explanation: Short factual reasoning with sources if possible.

#     Claim: "{claim}"
#     """
#     try:
#         response = gemini_model.generate_content(prompt)
#         return clean_text(response.text)
#     except Exception as e:
#         return f"Error: Gemini check failed: {e}"

# agent = get_agent()




# # ================== Title ==================
# st.markdown(
#     """
#     <h2 style='
#         text-align: center;
#         background: linear-gradient(90deg, #4facfe, #00f2fe, #43e97b, #f8ffae);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-weight: bold;
#         font-size: 2em;
#         margin-bottom: 10px;
#     '>
#         🕵️ FactChecker Bot
#     </h2>
#     """,
#     unsafe_allow_html=True
# )

# # ================== Session State ==================
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "show_uploader" not in st.session_state:
#     st.session_state.show_uploader = False

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# # Initialize send_clicked to avoid AttributeError
# if "send_clicked" not in st.session_state:
#     st.session_state.send_clicked = False

# # ================== Sidebar ==================
# with st.sidebar:
#     st.markdown(
#         f"""
#         <div style='text-align: center; margin-bottom: 20px;'>
#             <img src='{LOGO_URL}' width='120' height='80' style='border-radius: 10px;'>
#         </div>
#         """, 
#         unsafe_allow_html=True
#     )
    
#     st.markdown("<h3 style='text-align: left; color: linear-gradient(90deg, #4facfe, #00f2fe, #43e97b, #f8ffae)'>📝 Sample Claims to Try</h3>", unsafe_allow_html=True)
#     st.markdown("<div style='text-align: left;'>", unsafe_allow_html=True)

#    # ---------------- Sidebar Claims ----------------
#     claims = [
#         "Delhi is the capital of India.",
#         "The moon is made of cheese.",
#         "Water boils at 100°C at sea level.",
#         "Mount Everest is the tallest mountain in the world.",
#         "Sharks are mammals.",
#         "The Great Wall of China is visible from space.",
#         "Bananas grow on trees.",
#         "The Pacific Ocean is the largest ocean on Earth.",
#         "Humans have walked on Mars.",
#         "Lightning never strikes the same place twice."
#     ]

#     for idx, claim in enumerate(claims):
#         if st.button(claim, key=f"claim_{idx}"):
#             st.session_state.user_input = claim  # Automatically fill input box
#             st.session_state.send_clicked = True  # Trigger sending



    


# # ================== Display Chat History ==================
# for message in st.session_state.chat_history:
#     if message["bot"]:
#         st.markdown(
#             f"""
#             <div style='display: flex; align-items: flex-start; margin-bottom: 12px;'>
#                 <img src="{BOT_AVATAR}" width="50" height="50" style="border-radius:50%; margin-right:10px;">
#                 <div style='background: #f4f4f4; padding: 12px 18px; border-radius: 12px; max-width: 70%; color: black;'>
#                     {message['bot']}
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     if message["user"]:
#         st.markdown(
#             f"""
#             <div style='display: flex; justify-content: flex-end; margin-bottom: 12px;'>
#                 <div style='background: linear-gradient(145deg, #4facfe, #00f2fe); color: white; padding: 12px 18px; border-radius: 12px; max-width: 70%;'>
#                     {message['user']}
#                 </div>
#                 <img src="{USER_AVATAR}" width="50" height="50" style="border-radius:50%; margin-left:10px;">
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# st.markdown("---")
# # Create columns for upload button, input box, and send button
# col_upload, col_input, col_send = st.columns([0.1, 0.75, 0.15])

# # Upload button
# with col_upload:
#     if st.button("➕", help="Attach file"):
#         st.session_state.show_uploader = not st.session_state.show_uploader

# # Input box
# with col_input:
#     user_input = st.text_input(
#         label="",
#         value=st.session_state.user_input,
#         placeholder="Type your claim here...",
#         key="main_input",
#         label_visibility="collapsed"
#     )

# # Send button
# with col_send:
#     send_clicked = st.button("➤", help="Send")

# # Optional: file uploader appears only if toggled
# uploaded_file = None
# if st.session_state.show_uploader:
#     uploaded_file = st.file_uploader(
#         "Upload a file or image",
#         type=["txt", "pdf", "png", "jpg", "jpeg"],
#         label_visibility="collapsed"
#     )


# # ---------------- Handle Sending ----------------
#     if (send_clicked or st.session_state.send_clicked) and st.session_state.user_input.strip():
#         with st.spinner("Fact-checking..."):
#             bot_response = fact_check_claim_with_gemini(st.session_state.user_input)
#         st.session_state.chat_history.append({
#             "user": st.session_state.user_input,
#             "bot": bot_response
#         })
#         # Reset send_clicked
#         st.session_state.send_clicked = False
#         st.session_state.user_input = ""  # Clear input box
#         st.rerun()  # Refresh to show new message







# streamlit_app1.py
import os
import re
import streamlit as st
from src.agent_wrapper import get_agent
from google.generativeai import configure, GenerativeModel

# ================== Page Config ==================
st.set_page_config(page_title="FactChecker Bot", layout="wide")

# ================== API Config ==================
API_KEY = os.getenv("GOOGLE_API_KEY", "your_api_key_here")
configure(api_key=API_KEY)
gemini_model = GenerativeModel("gemini-2.5-flash")

# ================== Gemini Initialization ==================
def clean_text(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    return text.strip()

# ================== Fact-Checking Function ==================
def fact_check_claim_with_gemini(claim: str) -> str:
    prompt = f"""
    You are a fact-checking assistant. Verify the following claim and respond in the format:
    Verdict: True/False/Partially True
    Explanation: Short factual reasoning with sources if possible.

    Claim: "{claim}"
    """
    try:
        response = gemini_model.generate_content(prompt)
        return clean_text(response.text)
    except Exception as e:
        return f"Error: Gemini check failed: {e}"

agent = get_agent()

# ================== Title ==================
st.markdown(
    """
    <h2 style='
        text-align: center;
        background: linear-gradient(90deg, #4facfe, #00f2fe, #43e97b, #f8ffae);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 2em;
        margin-bottom: 10px;
    '>
        🕵️ FactChecker Bot
    </h2>
    """,
    unsafe_allow_html=True
)

# ================== Session State ==================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "show_uploader" not in st.session_state:
    st.session_state.show_uploader = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "send_clicked" not in st.session_state:
    st.session_state.send_clicked = False

# ================== Sidebar =================

LOGO_URL = "https://media.istockphoto.com/id/2178949438/vector/chatbot-icon-bot-sign-design-chatbot-logo-concept-robot-head-in-a-speech-bubble-online.jpg?s=612x612&w=0&k=20&c=_X5HzRHbp6PP6UIU2nsv86qxEJIpuwmqvEJ4V_pFnZc="
USER_AVATAR = "data:image/webp;base64,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"
BOT_AVATAR = "https://th.bing.com/th/id/OIP.3ffah5nxd1fBLy0g5xdKHQHaFs?w=274&h=211&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3"



claims = [
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
]

with st.sidebar:
    st.markdown(
        f"""
        <div style='text-align: center; margin-bottom: 20px;'>
            <img src='{LOGO_URL}' width='120' height='80' style='border-radius: 10px;'>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h3 style='color: #FF5733;'>📝 Sample Claims to Try</h3>", unsafe_allow_html=True)




    for idx, claim in enumerate(claims):
        button_id = f"claim_{idx}"

        # Style the button with CSS
        st.markdown(
            f"""
            <style>
            div.stButton > button#{button_id} {{
                text-align: left;
                background-color: #000000;
                color: white;
                padding: 8px 12px;
                margin-bottom: 6px;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 500;
                border: 1px solid #ccc;
                transition: background-color 0.3s;
                width: 100%;
            }}
            div.stButton > button#{button_id}:hover {{
                background-color: #333333;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Functional button
        if st.button(claim, key=button_id):
            # Do not try to set st.session_state[button_id]!
            st.session_state.user_input = claim
            st.session_state.send_clicked = True



    







# ================== Display Chat History ==================
for message in st.session_state.chat_history:
    if message.get("bot"):
        st.markdown(
            f"""
            <div style='display: flex; align-items: flex-start; margin-bottom: 12px;'>
                <img src="{BOT_AVATAR}" width="50" height="50" style="border-radius:50%; margin-right:10px;">
                <div style='background: #f4f4f4; padding: 12px 18px; border-radius: 12px; max-width: 70%; color: black;'>
                    {message['bot']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if message.get("user"):
        st.markdown(
            f"""
            <div style='display: flex; justify-content: flex-end; margin-bottom: 12px;'>
                <div style='background: linear-gradient(145deg, #4facfe, #00f2fe); color: white; padding: 12px 18px; border-radius: 12px; max-width: 70%;'>
                    {message['user']}
                </div>
                <img src="{USER_AVATAR}" width="50" height="50" style="border-radius:50%; margin-left:10px;">
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# ================== Main Input Box ==================
col_upload, col_input, col_send = st.columns([0.1, 0.75, 0.15])

with col_upload:
    if st.button("➕", help="Attach file"):
        st.session_state.show_uploader = not st.session_state.show_uploader

with col_input:
    user_input = st.text_input(
        label="Enter your claim",
        value=st.session_state.user_input,
        placeholder="Type your claim here...",
        key="main_input",
        label_visibility="collapsed"
    )

with col_send:
    send_clicked = st.button("➤", help="Send")

# Optional file uploader
uploaded_file = None
if st.session_state.show_uploader:
    uploaded_file = st.file_uploader(
        "Upload a file or image",
        type=["txt", "pdf", "png", "jpg", "jpeg"],
        label_visibility="collapsed"
    )

# ================== Handle Sending ==================
if (send_clicked or st.session_state.send_clicked) and user_input.strip():
    with st.spinner("Fact-checking..."):
        if uploaded_file:
            st.warning("File processing not yet implemented.")
        bot_response = fact_check_claim_with_gemini(user_input)

    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
    st.session_state.user_input = ""  # clear input
    st.session_state.send_clicked = False
    st.rerun()
