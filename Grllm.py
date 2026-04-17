from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("GROQ_API_KEY"))

llm = ChatGroq(
    model="llama3-8b-8192"
)

response = llm.invoke("Explain Artificial Intelligence in simple words")

print(response.content)