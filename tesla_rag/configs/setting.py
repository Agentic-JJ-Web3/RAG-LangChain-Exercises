import os
import requests
from dotenv import load_dotenv, find_dotenv
from pprint import pprint
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def environement_variables():
    load_dotenv(find_dotenv())
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
   
    # print("API KEYS LOADING...")
    # pprint(GOOGLE_API_KEY)

def load_google_llm():
    # loading our keys
    environement_variables()
    google_llm = GoogleGenerativeAI(
        # pass our configurations here
        model="gemini-2.5-flash", 
        temperature=0.7
        )
    return google_llm

def load_google_chat_model():
    environement_variables()
    google_chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return google_chat


def load_embeddings():
    environement_variables()
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Test with sample text
    # Embeddings work by converting text to numerical representations(vectors) that capture meaning

    # sample_text = [
    #     "The weather is beautiful today.",
    #     "It's a sunny and pleasant day outside.",
    #     "I love going for walks when the weather is nice.",
    #     "Machine learning is fascinating."
    #     ]
    
    # print("Generating embeddings for sample text...")
    # print("-"*50)

    # Generate embeddings for multiple texts at once
    # This is more efficient than generating them one by one
    # embedded_docs = embeddings.embed_documents(sample_text)
    return embeddings
