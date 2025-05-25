import os
import streamlit as st
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

def load_answer(question):
    """Return the response from the language model for a given question."""
    return cloud_llm.invoke(question)

def get_text():
    """Get user input from Streamlit text input."""
    return st.text_input("You: ", key="input")
