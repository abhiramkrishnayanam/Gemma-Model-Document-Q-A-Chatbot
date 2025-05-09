import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings #Vector embedding technique

import time
import os
from tempfile import NamedTemporaryFile

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
groq_api_key = st.secrets["GROQ_API_KEY"]

# Streamlit App UI
# --------------------------
st.title("📄 Gemma Model Document Q&A")

#Initialize Groq LLM
llm=ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

#Prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided content only.
    Please provide the most accurate response based on the question.
    
    <context>
    {context}
    </context>
    
    Question: {input}
    """
)

#Upload PDF
uploaded_file= st.file_uploader("📤 Upload a PDF file", type=["pdf"])

#Vector store creation
if uploaded_file and st.button("⚙️ Create Vector Store from Uploaded PDF"):
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    #load PDF and split into chunks
    loader = PyPDFLoader(tmp_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)

    #Create embeddings and FAISS vector store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    st.session_state.vectors = FAISS.from_documents(final_documents, embeddings)
    st.success("✅ Vector store created successfully!")

#Question input
prompt1 = st.text_input("💬 Ask a question based on the uploaded PDF")
if prompt1 and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retriever_chain.invoke({'input' : prompt1})
    st.write("Answer : ", response['answer'])

    with st.expander("🔍 Document Similarity Chunks"):
        for i, doc in enumerate(response["context"]):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(doc.page_content)
            st.write("------")
