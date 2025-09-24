from configs import load_embeddings
from pprint import pprint
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, WikipediaLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Step 0: Embeddings
embeddings = load_embeddings()
os.environ["USER_AGENT"] = "tesla_rag_app"
# ========================
# Step 1: Load Documents
# ========================

# 1. Load Multiple PDFs
pdf_files = [
    "./data/2021-tesla-impact-report.pdf",
    "./data/2023-tesla-impact-report-highlights.pdf"
]
docs_from_pdfs = []
for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    docs_from_pdfs.extend(loader.load())

# 2. Load from Websites
urls = [
    "https://www.tesla.com/about",
    "https://www.spacex.com/"
]
docs_from_web = []
print('Searching the web..')
for url in urls:
    loader = WebBaseLoader(url)
    docs_from_web.extend(loader.load())

# 3. Load from Wikipedia
print('Searching Wikipedia..')
wiki_loader = WikipediaLoader(query="Tesla, Inc.", load_max_docs=2)
docs_from_wiki = wiki_loader.load()

# Combine all
all_docs = docs_from_pdfs + docs_from_web + docs_from_wiki
print(f"Total documents loaded: {len(all_docs)}")

# ========================
# Step 2: Split Documents
# ========================
# text_splitter = CharacterTextSplitter(
#     separator="\n\n",
#     chunk_size=1000,
#     chunk_overlap=200,
#     length_function=len,
#     is_separator_regex=False
# )
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", "!", "?", " ", ""]
)

docs = text_splitter.split_documents(all_docs)
print(f"Total chunks created: {len(docs)}")

# ========================
# Step 3: Vector Store
# ========================
persist_dir = "./chroma_db"
if not os.path.exists(persist_dir):
    os.makedirs(persist_dir)

vector_db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)
vector_db.persist()

# ========================
# Step 4: Query
# ========================
prompt = "Was Tesla profitable? List some key metrics from their reports and Wikipedia."
response = vector_db.similarity_search(prompt, k=3)
print('Printing response to semantic search')
print('='*60)

pprint(response)
