import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import NEWS_API_KEY, GOOGLE_API_KEY
from app.news_loader import NewsLoader
from app.ai_enhancer import enhance_article

loader = NewsLoader(api_key=NEWS_API_KEY, query="AI in healthcare")
documents = loader.load()

if documents:
    article_content = documents[0].page_content
    
    if article_content and article_content != 'ONLY AVAILABLE IN PAID PLANS':
        enhancement = enhance_article(article_content, GOOGLE_API_KEY)
        print(enhancement)
    else:
        print("Article content is not available for enhancement.")
