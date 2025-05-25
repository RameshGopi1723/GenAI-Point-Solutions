import streamlit as st
from langchain.schema import SystemMessage
from helpers import get_text, load_answer


def main():
    st.set_page_config(page_title="LangChain Convo Bot", page_icon=":robot:")
    st.header("Hey, I'm your Chat GPT")

    if "sessionMessages" not in st.session_state:
        st.session_state.sessionMessages = [
            SystemMessage(content="You are a Sarcastic and Thug life assistant.")
        ]

    user_input=get_text()
    submit = st.button('Generate')  

    if submit:
        response = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response)


if __name__ == "__main__":
    main()