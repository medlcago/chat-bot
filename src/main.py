import streamlit as st

from chatbot import ChatBot
from config import config

st.set_page_config(page_title="Chat", layout="wide")

st.title("***Chat Bot***", anchor=False)
selected_model = st.selectbox("Select Model Type", config.model_config.available_models, label_visibility="collapsed")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "Привет, как я могу тебе помочь?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Введите ваш запрос"):
    with st.spinner("Обработка запроса..."):
        st.chat_message("user").write(prompt)
        content = st.chat_message("ai").write_stream(
            ChatBot(
                prompt=prompt,
                model=selected_model
            )
            .ask(stream=True)
        )
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "ai", "content": content})
