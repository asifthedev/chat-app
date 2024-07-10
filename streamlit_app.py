import os
import streamlit as st
from openai import OpenAI

st.title("GPT Clone")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if "message" not in st.session_state:
    st.session_state["message"] = []
else:
    for message in st.session_state["message"]:
        with st.chat_message(message['role']):
            st.markdown(message['content'], unsafe_allow_html=True)

prompt = st.chat_input("What is up?")

if prompt:
    conversation = [{'role': "system",
                     'content': "Assume you are an expert with over 10 years of experience in Ubuntu operating system administration."},
                    {'role': "user", 'content': prompt}]

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=conversation,
        max_tokens=500
    )

    with st.chat_message("user"):
        st.markdown(prompt, unsafe_allow_html=True)

    st.session_state["message"].append({'role': "user", 'content': prompt})

    with st.chat_message("assistant"):
        st.markdown(response.choices[0].message.content, unsafe_allow_html=True)