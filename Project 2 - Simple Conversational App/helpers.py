import os
import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the language model
cloud_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


def get_text():
    """Get user input from Streamlit text input."""
    input_text = st.text_input("You: ")
    return input_text


def load_answer(question):
    """Return the response from the language model for a given question."""
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer  = cloud_llm.invoke(st.session_state.sessionMessages )
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content