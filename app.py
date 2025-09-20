import streamlit as st 
prompt = st.chat_input("say somthing...")


if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(f"you said: {prompt}")    
        