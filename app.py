import streamlit as st
from chatbot_engine import get_response, init_session_state

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot")

init_session_state()

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask the AI Assistant..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
