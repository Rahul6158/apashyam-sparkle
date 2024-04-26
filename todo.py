import streamlit as st

# Initialize empty list to store messages
messages = []

# Sidebar to enter username
username = st.sidebar.text_input("Enter Your Username")

# Main chat interface
st.title("Chat Room")

# Text area to display chat history
chat_history = st.text_area("Chat History:", height=400, value="")

# Text input for entering new message
new_message = st.text_input("Enter Message:")

# Button to send message
if st.button("Send"):
    if new_message:
        message = f"{username}: {new_message}"
        messages.append(message)

# Display updated chat history
if messages:
    for message in messages:
        st.write(message)
else:
    st.write("No messages yet.")
