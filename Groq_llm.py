from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv(".env")


llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

response = llm.invoke("Explain Artificial Intelligence in simple words")

print(response.content)