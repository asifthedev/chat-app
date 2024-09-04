import os
import streamlit as st
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Configuration and Initialization
st.title("Python :red[Assitant]")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if "message" not in st.session_state:
    st.session_state["message"] = []

# Function Definitions
def linux_admin() -> object:
    conversation = [
        {'role': "system", 'content': "You are a python code assitant who helps the students whe they are facing python related errors in their code"},
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
