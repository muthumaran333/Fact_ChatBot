# import streamlit as st
# from src.prompt_chains import FactCheckChain
# from src import utils

# # -----------------------------
# # Page Setup
# # -----------------------------
# st.set_page_config(page_title="FactChecker Bot", layout="wide")
# st.title("🕵️ FactChecker Bot")
# st.markdown("Enter a claim below, and the bot will check its validity.")

# # -----------------------------
# # Initialize FactCheckChain
# # -----------------------------
# chain = FactCheckChain()

# # -----------------------------
# # User Input
# # -----------------------------
# claim = st.text_area("Enter your claim:", height=100)

# if st.button("Check Claim") and claim.strip():
#     st.info("Processing claim...")
    
#     # Step 1: Clean the claim
#     cleaned_claim = utils.clean_text(claim)
    
#     # Step 2: Check cache
#     cached_result = utils.load_cache(cleaned_claim)
    
#     if cached_result:
#         st.success("Result retrieved from cache.")
#         final_result = cached_result
#     else:
#         # Step 3: Run fact-check chain
#         initial_resp = chain.initial_response(cleaned_claim)
#         assumptions = chain.extract_assumptions(initial_resp)
#         evidence_summary = "\n".join(assumptions)  # placeholder for real evidence
#         final_result = chain.final_synthesis(evidence_summary)
#         utils.save_cache(cleaned_claim, final_result)
    
#     # Step 4: Display results
#     st.subheader("📝 Fact Check Result")
#     st.write(utils.format_fact_check_result(cleaned_claim, final_result))
    
#     st.subheader("🔹 Initial Response")
#     st.write(initial_resp)
    
#     st.subheader("🔹 Extracted Assumptions")
#     st.write(assumptions)
    
#     st.subheader("🔹 Evidence Summary")
#     st.write(evidence_summary)



import streamlit as st
from src.prompt_chains import FactCheckChain
from src import utils

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="FactChecker Bot", layout="wide")
st.title("🕵️ FactChecker Bot")
st.markdown("Enter a claim below, and the bot will check its validity like a conversation!")

# -----------------------------
# Initialize FactCheckChain
# -----------------------------
chain = FactCheckChain()

# -----------------------------
# Initialize session state for chat history
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # each entry: {"user": ..., "bot": ...}

# -----------------------------
# User Input
# -----------------------------
claim = st.text_input("Enter your claim:", "")

if st.button("Send") and claim.strip():
    cleaned_claim = utils.clean_text(claim)
    
    # Check cache first
    cached_result = utils.load_cache(cleaned_claim)
    if cached_result:
        final_result = cached_result
    else:
        # Run fact-check chain
        initial_resp = chain.initial_response(cleaned_claim)
        assumptions = chain.extract_assumptions(initial_resp)
        evidence_summary = "\n".join(assumptions)  # placeholder for real evidence
        final_result = chain.final_synthesis(evidence_summary)
        utils.save_cache(cleaned_claim, final_result)
    
    # Add to chat history
    st.session_state.chat_history.append({
        "user": claim,
        "bot": final_result
    })

# -----------------------------
# Display chat history
# -----------------------------
st.subheader("💬 Chat History")
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
