from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
import requests
from typing import List

class NewsLoader(BaseLoader):
    """A custom loader for fetching news from the NewsData.io API."""

    def __init__(self, api_key: str, query: str):
        self.api_key = api_key
        self.query = query

    def load(self) -> List[Document]:
        """Load news articles from the API and convert them to Documents."""
        url = f"https://newsdata.io/api/1/news?apikey={self.api_key}&q={self.query}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")

        results = response.json().get("results", [])
        documents = []
        for article in results:
            doc = Document(
                page_content=article.get("content", ""),
                metadata={
                    "title": article.get("title"),
                    "link": article.get("link"),
                    "source": article.get("source_id"),
                    "publish_date": article.get("pubDate"),
                },
            )
            documents.append(doc)
        
        return documents
