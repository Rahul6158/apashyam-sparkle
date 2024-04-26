import streamlit as st
import secrets
import SessionState

# Define secret code
secret_code = str(secrets.randbelow(10000)).zfill(4)

# Define session state
session_state = SessionState.get(page=1, entered_code="")

# Page 1: Generate Secret Code or Enter Secret Code
if session_state.page == 1:
    st.title("Secret Code Chat App")
    if st.button("Generate Secret Code"):
        st.write("Your secret code is:", secret_code)
    if st.button("Enter Secret Code"):
        session_state.page = 2

# Page 2: Chat Room
elif session_state.page == 2:
    st.title("Chat Room")
    st.write("Enter the secret code to join the chat:")
    entered_code = st.text_input("Secret Code")
    if st.button("Enter"):
        if entered_code == secret_code:
            st.write("You have entered the correct secret code.")
            st.write("Chat room opened. Start chatting!")
            session_state.page = 3
        else:
            st.write("Incorrect secret code. Please try again.")

# Page 3: Chatting Interface
elif session_state.page == 3:
    st.title("Chat Room")
    st.write("Chat interface goes here...")

    # Example chat interface using text_input and st.write
    message = st.text_input("Type your message")
    if st.button("Send"):
        st.write("You:", message)
