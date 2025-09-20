import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import NEWS_API_KEY
from app.news_loader import NewsLoader

loader = NewsLoader(api_key=NEWS_API_KEY, query="Tesla")

documents = loader.load()

print(f"Loaded {len(documents)} documents")

if documents:
    print(documents[0])
