import streamlit as st

# Sample dictionary containing prompt-response pairs (you can modify this as needed)
prompt_response_dict = {
    "prompt-1": "response-1",
    "prompt-2": "response-2",
    "prompt-3": "response-3",
    "prompt-4": "response-4",
    "prompt-5": "response-5"
}

# Function to generate a response based on user input
def get_response(user_input):
    # Check if the user input matches a prompt in the dictionary
    for prompt, response in prompt_response_dict.items():
        if user_input.lower() in prompt.lower():  # Case-insensitive matching
            return response
    # Default response if no match is found
    return "I'm here to assist! Let me know how I can help."

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
