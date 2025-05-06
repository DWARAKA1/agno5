import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is not set. Please check your .env file.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit app
st.title("Groq Chat Completion App")

# Input from the user
user_input = st.text_area("Enter your prompt:", placeholder="Type your message here...")

# Placeholder for the response
response = None

if st.button("Generate Response"):
    if user_input.strip():
        try:
            # Call the Groq API
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )
            # Display the response
            response = completion.choices[0].message.content
            st.subheader("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before generating a response.")

# Save response button
if response:
    if st.button("Save Response"):
        try:
            with open("response.txt", "w", encoding="utf-8") as file:
                file.write(response)
            st.success("Response saved to response.txt")
        except Exception as e:
            st.error(f"An error occurred while saving the response: {e}")