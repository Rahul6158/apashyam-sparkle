import streamlit as st
from datetime import datetime

# Initialize empty lists to store messages
chat_history_user1 = []
chat_history_user2 = []

# Sidebar to enter usernames
with st.sidebar:
    user1 = st.text_input("User 1", "User 1")
    user2 = st.text_input("User 2", "User 2")

# Main chat interface
st.title("Chat Room")

# Text area to display chat history for User 1
st.subheader(f"Chat History for {user1}:")
for chat in chat_history_user1:
    st.write(f"{chat['timestamp']} - {chat['user']}: {chat['message']}")

# Text area to display chat history for User 2
st.subheader(f"Chat History for {user2}:")
for chat in chat_history_user2:
    st.write(f"{chat['timestamp']} - {chat['user']}: {chat['message']}")

# Text input for entering new message
new_message = st.text_input("Enter Message:")

# Button to send message
if st.button("Send"):
    if new_message:
        timestamp = datetime.now().strftime("%H:%M:%S")
        chat_history_user1.append({"timestamp": timestamp, "user": user1, "message": new_message})
        chat_history_user2.append({"timestamp": timestamp, "user": user2, "message": new_message})

