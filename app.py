
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from groq import Groq

# Retrieve the API key from the environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")

client = Groq(api_key=GROQ_API_KEY)
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)