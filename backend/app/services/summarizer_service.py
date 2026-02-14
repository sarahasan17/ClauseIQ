import tempfile
import os
import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from llama_index.readers.file import PDFReader
from langchain_groq import ChatGroq
from app.core.config import settings

# Initialize Groq LLaMA model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY
)


def extract_text_from_pdf(pdf_file) -> str:
    """Extracts structured text from a legal contract PDF.
       Expects a file-like object."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_file.read())
        tmp_path = tmp.name
    pdf_reader = PDFReader()
    documents = pdf_reader.load_data(tmp_path)
    extracted_text = "\n\n".join(doc.text for doc in documents)
    os.remove(tmp_path)
    return extracted_text.strip()

def chunk_text(text: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len
    )
    return text_splitter.split_text(text)

def summarize_text(text_chunk: str) -> str:
    prompt = f"""
    Summarize the following legal document content in a clear and concise way:
    
    {text_chunk}

    Return the summary in proper HTML format, including paragraphs, and lists when necessary.
    """
    response = llm.invoke(prompt)
    return response.content

def generate_summary_from_pdf(pdf_file) -> str:
    """Combines text extraction, chunking, and summarization."""
    full_text = extract_text_from_pdf(pdf_file)
    chunks = chunk_text(full_text)
    summaries = [summarize_text(chunk) for chunk in chunks]
    return "\n\n".join(summaries)
