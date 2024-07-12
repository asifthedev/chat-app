import os
import streamlit as st
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Configuration and Initialization
st.title("Linux :red[Administrator]")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if "message" not in st.session_state:
    st.session_state["message"] = []

# Function Definitions
def linux_admin() -> object:
    conversation = [
        {'role': "system", 'content': "Assume you are a chat bot who's expert with over 10 years of experience in Linux operating system administration. And a student who's curious and want to clear his doubts chatting with you on WhatsApp. Do not forget to include bash code example while answering. Note keep your answer short and concise as possible "},
        {'role': "user", 'content': prompt}
    ]
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-16k',
        messages=conversation,
        temperature=1,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

# Main Application Logic
for message in st.session_state["message"]:
    with st.chat_message(message['role']):
        st.markdown(message['content'], unsafe_allow_html=True)

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt, unsafe_allow_html=True)
    st.session_state["message"].append({'role': "user", 'content': prompt})

    with st.spinner("typing..."):
        response = linux_admin()

    bot_ans = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(bot_ans, unsafe_allow_html=True)
    st.session_state["message"].append({'role': "assistant", 'content': bot_ans})
