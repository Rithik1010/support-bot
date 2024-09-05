import openai
import streamlit as st
import re

if not st.secrets.get("api_key") or not st.secrets.get("assistant_id"):
    st.error("API key or Assistant ID is missing in the configuration.")
    st.stop()  # Stop execution if credentials are missing

openai.api_key = st.secrets["api_key"]
assistant_id = st.secrets["assistant_id"]
pattern = r'【\d+:\d+†source】'

# An object that allows our python application to interact with the OpenAI API
client = openai

st.set_page_config(page_title="Support Bot", page_icon=":speech_balloon:")
st.title("💬 Support Bot")
st.caption("🚀 AI-powered bot providing responses from a knowledge base to user queries.")

if "thread_id" not in st.session_state:
    try:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id
    except openai.error.OpenAIError as e:
        st.error(f"Failed to create a thread: {e}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # cleaned_text = re.sub(pattern, '', message["content"])
        st.markdown(message["content"])

def stream_generator():
    try:
        stream = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant_id,
            stream=True
        )

        for event in stream:
            if(event.data.object == "thread.message.delta"):
                for content in event.data.delta.content:
                    if content.type == "text":
                        yield re.sub(pattern, '', content.text.value)

    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")
        return

if prompt := st.chat_input("Enter you message"):
    if prompt.strip() == "":
        st.warning("Input cannot be empty!")
    else:
        with st.chat_message("user"):
            st.markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})

        client.beta.threads.messages.create(
            thread_id=st.session_state.thread_id,
            role="user",
            content=prompt
        )

        with st.chat_message("assistant"):           
            response = st.write_stream(stream_generator())  
            
        st.session_state.messages.append({"role": "assistant", "content": response})