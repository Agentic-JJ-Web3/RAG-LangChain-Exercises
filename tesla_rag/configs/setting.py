from langchain.llms import GooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from dotenv import load_dotenv
import os

def load_env():
    """Load environment variables from .env file"""
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found in environment variables")

def get_llm():
    """Initialize and return Google Gemini LLM"""
    return GooglePalm(
        temperature=0.7,
        model_name="gemini-pro"
    )

def get_embeddings():
    """Initialize and return Google Palm embeddings"""
    return GooglePalmEmbeddings()