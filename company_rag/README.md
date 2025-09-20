# Exercise 2: Organization RAG System

This project will guide you through building a complete Retrieval-Augmented Generation (RAG) system from scratch.

## Goal

The objective is to create a command-line assistant that can answer questions about a specific organization (e.g., Tesla, NASA). The system will use a curated knowledge base of documents and web pages, ensuring the answers are based on factual data.

## Core Concepts to Learn

*   **Data Loading:** Loading data from diverse sources like web pages, PDF files, and Wikipedia.
*   **Document Chunking:** Splitting large documents into smaller, manageable chunks for efficient processing.
*   **Vector Stores:** Using a vector database (ChromaDB) to store and index the document chunks for fast retrieval.
*   **Retrieval:** Finding the most relevant document chunks for a user's question.
*   **Response Generation:** Using an LLM (Gemini) to generate a natural language answer based on the retrieved information.
*   **RAG Pipeline:** Chaining all the above components together to form a complete question-answering system.

## Our Step-by-Step Plan

1.  **Project Setup:** Create a Python virtual environment and install the necessary libraries (LangChain, ChromaDB, etc.).
2.  **Choose Organization:** Select a data-rich organization to be the subject of our RAG system.
3.  **Data Loading:** Use LangChain loaders to collect data from the organization's website, Wikipedia page, and relevant PDF documents.
4.  **Chunking:** Split the loaded documents into smaller chunks using a text splitter.
5.  **Vector Store Creation:** Create a ChromaDB vector store and embed the document chunks into it.
6.  **Build the RAG Chain:** Construct the full RAG pipeline that takes a user's question, retrieves relevant documents, and generates an answer with the LLM.
7.  **Create CLI:** Develop a simple command-line interface (CLI) for interacting with the RAG system.
8.  **Testing:** Thoroughly test the system's ability to answer questions accurately and handle off-topic queries.
