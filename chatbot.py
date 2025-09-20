import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from backend import generate_response  


st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")


st.markdown("""
    <style>
        .user-msg {
            
            background-color:#949494;
            color: white;
            padding: 10px;
            border-radius: 12px;
            margin: 5px;

            *//display: flex;
            justify-content: flex-end;
            align-self: flex-end;
            max-width: 80%;*//
        }
        .bot-msg {
            background-color: RGB(70, 50, 100);
            color: white;
            padding: 10px;
            border-radius: 12px;
            margin: 5px 0px;
        }
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin: -1rem -1rem  2rem -1rem;
            border-radius: 10px;
        }

    </style>
""", unsafe_allow_html=True)

st.markdown( "<div class='main-header'><h1 style='text-align: center;'>Chatbot</h1></div>", unsafe_allow_html=True)


with st.sidebar:
    st.subheader("Quick Questions")
    if st.button(" how this work ?", use_container_width=True):
        st.session_state.quick_prompt = "How this work ?"
    if st.button(" What can you do?", use_container_width=True):
        st.session_state.quick_prompt = "What can you do?"
    if st.button(" Explain Streamlit", use_container_width=True):
        st.session_state.quick_prompt = "Explain Streamlit in simple terms."
    st.divider()
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []


if "messages" not in st.session_state: 
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant. Answer clearly and concisely.")
    ]


for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.markdown(f"<div class='user-msg'> {message.content}</div>", unsafe_allow_html=True)
    elif isinstance(message, AIMessage):
        st.markdown(f"<div class='bot-msg'> {message.content}</div>", unsafe_allow_html=True)


prompt = st.chat_input("Type your message...")

if "quick_prompt" in st.session_state and st.session_state.quick_prompt:
    prompt = st.session_state.quick_prompt
    st.session_state.quick_prompt = None

if prompt:

    st.markdown(f"<div class='user-msg'> {prompt}</div>", unsafe_allow_html=True)
    st.session_state.messages.append(HumanMessage(prompt))

    with st.spinner(" Thinking..."):
        placeholder = st.empty()
        response = ""
        for partial in generate_response(st.session_state.messages):
            response = partial
            placeholder.markdown(f"<div class='bot-msg'> {response}▌</div>", unsafe_allow_html=True)
        placeholder.markdown(f"<div class='bot-msg'> {response}</div>", unsafe_allow_html=True)

    st.session_state.messages.append(AIMessage(response))
