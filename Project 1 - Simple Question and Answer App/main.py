import streamlit as st
from helpers import get_text, load_answer


def main():
    st.set_page_config(page_title="LangChain Q/A App", page_icon=":robot:")
    st.header("LangChain Demo - Basic ChatBot")

    user_input = get_text()
    submit = st.button('Generate')

    if submit:
        response = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response.content)


if __name__ == "__main__":
    main()