import streamlit as st

# Load and execute code from App.py
with open("App.py") as file:
    exec(file.read())

# Streamlit App
st.title("Chat with TravelBot")

# Chat History
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**{sender}:** {message}")
    else:
        st.markdown(f"*{sender}:* {message}")

# User Input
user_input = st.text_input("Enter your message:", key="user_input")

if st.button("Send"):
    if user_input:
        # Add user input to chat history
        st.session_state.chat_history.append(("User", user_input))
        # Generate and add a response to chat history
        response = get_response(user_input)
        st.session_state.chat_history.append(("TravelBot", response))

# Clear chat history
if st.button("Clear Chat"):
    st.session_state.chat_history = []
