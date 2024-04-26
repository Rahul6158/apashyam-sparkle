import streamlit as st
from streamlit_shared.state import get_state
from datetime import datetime

# Initialize shared state
state = get_state(my_message="", other_message="", chat_history=[])

# Sidebar to enter usernames
with st.sidebar:
    my_username = st.text_input("Your Username", "User 1")
    other_username = st.text_input("Other Username", "User 2")

# Main chat interface
st.title("Chat Room")

# Display chat history
if state.chat_history:
    for chat in state.chat_history:
        st.write(f"{chat['timestamp']} - {chat['username']}: {chat['message']}")

# Text input for entering new message
new_message = st.text_input("Enter Message")

# Button to send message
if st.button("Send"):
    if new_message:
        timestamp = datetime.now().strftime("%H:%M:%S")
        state.chat_history.append({"timestamp": timestamp, "username": my_username, "message": new_message})

# Display other user's message
if state.other_message:
    st.write(f"{state.other_message['timestamp']} - {state.other_message['username']}: {state.other_message['message']}")

# Update other user's message
if st.checkbox("Update Other User's Message"):
    state.other_message = {"timestamp": datetime.now().strftime("%H:%M:%S"), "username": other_username, "message": new_message}
