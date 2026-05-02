import streamlit as st

st.set_page_config(
    page_title="Farah's Chat App",
    page_icon="💬"
)

def get_reply(user_message):
    message = user_message.lower()

    if "hi" in message or "hello" in message:
        return "Hi! Welcome to my chat app."

    elif "how are you" in message:
        return "I am good. Thanks for asking!"

    elif "streamlit" in message:
        return "Streamlit is what I used to make this app."

    elif "api" in message or "llm" in message:
        return "This app does not use an API or real AI."

    else:
        return "You said: " + user_message


st.title("💬 Farah's Chat App")

st.write("This is a simple chat app I made with Python and Streamlit.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_text = st.chat_input("Write a message")

if user_text:
    st.session_state.messages.append({
     "role": "user",
        "content": user_text
    })

    with st.chat_message("user"):
        st.write(user_text)

    reply = get_reply(user_text)
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    with st.chat_message("assistant"):
        st.write(reply)