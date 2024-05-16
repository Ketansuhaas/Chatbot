import streamlit as st
import time

st.set_page_config(page_title="Chat with the Streamlit docs, powered by LlamaIndex", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("NourishedChat")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Ask me a question about health and nutrition!"})
    
prompt = st.chat_input("Your question")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)  # Faking response generation
            response = "this is the response" 
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message) # Add response to message history
