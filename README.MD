# Farah's Chat App

This is a simple ChatGPT-style chat app built with Python and Streamlit.

## About the App

The app allows a user to type messages and receive mock assistant replies.

It does not use any external LLM, AI model, or third-party API.  
The replies are generated locally using a simple Python function.

## Features

- Built with Streamlit
- Uses `st.chat_input`
- Uses `st.chat_message`
- Stores chat history using `st.session_state.messages`
- Uses mock response logic
- Runs locally with Streamlit

## How to Run

First install Streamlit:

```bash
py -m pip install streamlit