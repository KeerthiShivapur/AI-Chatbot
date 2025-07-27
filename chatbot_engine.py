from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda

llm = ChatOllama(model="llama3")
chain = RunnableLambda(lambda messages: llm.invoke(messages))

def get_response(user_input: str) -> str:
    return chain.invoke(
        [HumanMessage(content=user_input)]
    ).content

def init_session_state():
    import streamlit as st
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
