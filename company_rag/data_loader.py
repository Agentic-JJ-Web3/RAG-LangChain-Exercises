
import os
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, WikipediaLoader

def load_data():
    # Load from a website
    web_loader = WebBaseLoader("https://www.tesla.com")
    web_docs = web_loader.load()

    # Load from PDFs in the data directory
    pdf_docs = []
    data_dir = "data"
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(data_dir, filename)
            pdf_loader = PyPDFLoader(pdf_path)
            pdf_docs.extend(pdf_loader.load())

    # Load from Wikipedia
    wiki_loader = WikipediaLoader(query="Tesla, Inc.", load_max_docs=1)
    wiki_docs = wiki_loader.load()

    return web_docs + pdf_docs + wiki_docs

if __name__ == "__main__":
    docs = load_data()
    print(f"Loaded {len(docs)} documents.")
