# Gemma Model Document Q&A Chatbot - Project Overview

This project is a document-based Q&A chatbot that allows users to upload a PDF, process its content, and ask questions based on the document. The chatbot utilizes Groq-based models, Langchain for document processing, and FAISS for efficient document retrieval.

## 🔄 Project Workflow

### 1. **User Uploads a PDF**
   - The user uploads a PDF document using the file uploader provided by Streamlit.
   - The system accepts only PDF file formats for processing.

### 2. **Document Parsing and Chunking**
   - Once the PDF is uploaded, it is parsed using the `PyPDFLoader`, which reads the document and extracts its text content.
   - The document is then split into smaller chunks using the `RecursiveCharacterTextSplitter`. This step ensures that the text is broken down into manageable portions, which helps in efficient processing and retrieval.

### 3. **Vector Store Creation**
   - After splitting the document into chunks, the text is transformed into embeddings using Google Generative AI Embeddings.
   - These embeddings are stored in a FAISS vector store, which is a data structure that enables fast similarity searches. This vector store allows the system to quickly retrieve relevant chunks of text in response to user queries.

### 4. **User Submits a Question**
   - After the vector store is created, the user can type a question related to the content of the uploaded PDF.
   - The system captures this question and prepares to find the most relevant document chunks based on the user's input.

### 5. **Question Answering Using Groq Model**
   - The question is passed to the Groq-based model (`gemma2-9b-it`), which is a large language model trained for accurate question answering.
   - The model processes the relevant document chunks retrieved from the vector store and generates an answer to the question.

### 6. **Display Answer and Context**
   - The generated answer is displayed to the user.
   - For transparency, the system also displays the document chunks that were used to generate the answer. This allows the user to see the context behind the response.

### 7. **Final Output**
   - The user sees the answer to their question along with the context (relevant document chunks) used to derive that answer.

## 🛠️ Technologies Used
- **Streamlit**: To create the interactive web app interface.
- **Langchain**: For document handling, text splitting, and model chaining.
- **Groq**: Used for the language model to provide accurate responses based on document content.
- **Google Generative AI Embeddings**: To convert document text into embeddings for similarity search.
- **FAISS**: For efficient retrieval of similar document chunks based on the user query.
- **PyPDFLoader**: For loading and extracting text from PDF files.

## 📝 Key Steps Recap
1. User uploads a PDF.
2. The document is parsed and split into chunks.
3. Embeddings are created and stored in a FAISS vector store.
4. User asks a question based on the PDF content.
5. The system uses Groq’s model to answer the question based on the retrieved document chunks.
6. The answer is displayed along with the context for transparency.

This process enables users to interact with large documents in a way that allows quick and precise question answering.

