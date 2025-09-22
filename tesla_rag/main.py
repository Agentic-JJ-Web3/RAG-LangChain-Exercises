import os
from pprint import pprint

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, WikipediaLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# ===============================
# Step 0: Config & Embeddings
# ===============================
# Make sure your Google Gemini API key is set:
# export GOOGLE_API_KEY="your_key_here"  (Linux/macOS)
# setx GOOGLE_API_KEY "your_key_here"   (Windows)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("⚠️ GOOGLE_API_KEY environment variable not set.")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-004")

# ===============================
# Step 1: Load Data Sources
# ===============================
print("📂 Loading data...")

# 1. PDFs
pdf_files = [
    "./data/2021-tesla-impact-report.pdf",
    "./data/2023-tesla-impact-report-highlights.pdf"
]
docs_from_pdfs = []
for pdf in pdf_files:
    if os.path.exists(pdf):
        loader = PyPDFLoader(pdf)
        docs_from_pdfs.extend(loader.load())
    else:
        print(f"⚠️ Skipping missing file: {pdf}")

# 2. Websites
urls = [
    "https://www.tesla.com/about",
    "https://www.tesla.com/impact"
]
docs_from_web = []
for url in urls:
    loader = WebBaseLoader(url)
    docs_from_web.extend(loader.load())

# 3. Wikipedia
wiki_loader = WikipediaLoader(query="Tesla, Inc.", load_max_docs=2)
docs_from_wiki = wiki_loader.load()

# Combine all
all_docs = docs_from_pdfs + docs_from_web + docs_from_wiki
print(f"✅ Total documents loaded: {len(all_docs)}")

# ===============================
# Step 2: Split Documents
# ===============================
print("✂️ Splitting into chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", "!", "?", " ", ""]
)

docs = splitter.split_documents(all_docs)
print(f"✅ Total chunks created: {len(docs)}")

# ===============================
# Step 3: Vector Store
# ===============================
print("🗄️ Creating Chroma DB...")

persist_dir = "./chroma_tesla"
vector_db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)

# ===============================
# Step 4: Boundary Enforcement
# ===============================
def is_about_org(question, org="Tesla"):
    return org.lower() in question.lower()

# ===============================
# Step 5: Retrieval QA
# ===============================
print("⚡ Initializing QA system...")

llm = GoogleGenerativeAI(model="gemini-pro")

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# ===============================
# Step 6: CLI
# ===============================
print("\n🤖 Welcome to Tesla Assistant!")
print("Ask questions about Tesla only (type 'quit' to exit).\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("👋 Goodbye!")
        break
    
    if not is_about_org(user_input, "Tesla"):
        print("Assistant: I only answer questions about Tesla.")
        continue
    
    result = qa_chain.invoke(user_input)
    print("\nAssistant:", result["result"])
    print("\n📚 Sources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source", "Unknown"))
    print("-" * 50)
