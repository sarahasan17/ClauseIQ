from fastapi.responses import HTMLResponse
import torch
import numpy as np
import re
from transformers import AutoModel, AutoTokenizer, pipeline
from langchain_groq import ChatGroq
from sklearn.metrics.pairwise import cosine_similarity
from huggingface_hub import login
from app.core.config import settings

# Authenticate with Hugging Face
login(token=settings.HUGGINGFACE_TOKEN)

# Load Legal-BERT for document understanding
legal_bert_model = "nlpaueb/legal-bert-base-uncased"
bert_tokenizer = AutoTokenizer.from_pretrained(legal_bert_model)
bert_model = AutoModel.from_pretrained(legal_bert_model)

# Load a pre-trained legal NER model
ner_pipeline = pipeline("ner", model="law-ai/InLegalBERT")

# Initialize Groq LLaMA for clause simplification
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY
)

def get_batch_legal_embeddings(texts: list) -> np.ndarray:
    """Efficiently encodes a batch of legal texts into embeddings."""
    inputs = bert_tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def extract_legal_keywords(text: str) -> list:
    """Extracts key legal terms using NER."""
    ner_results = ner_pipeline(text)
    extracted_terms = list(set([result['word'].replace("##", "") for result in ner_results]))
    return extracted_terms if extracted_terms else ["No significant legal terms detected"]

def extract_keywords_from_embedding(embedding: np.ndarray, reference_terms: list, text: str) -> list:
    """
    Matches embeddings to legal keywords using cosine similarity.
    Filters out terms that are not present in the original text.
    """
    embedding = embedding.reshape(1, -1)  # Ensure 2D shape
    reference_embeddings = get_batch_legal_embeddings(reference_terms)
    similarities = cosine_similarity(embedding, reference_embeddings)
    top_indices = np.argsort(similarities[0])[-3:]  # Top 3 matching legal concepts
    extracted_terms = [reference_terms[i] for i in top_indices]
    filtered_terms = [term for term in extracted_terms if term.lower() in text.lower()]
    return filtered_terms if filtered_terms else ["No significant legal terms detected"]

def simplify_legal_text_using_embeddings(embedding_keywords: list, original_text: str) -> str:
    """
    Simplifies the legal text based on extracted legal concepts.
    """
    prompt = f"""
    You are a legal expert specializing in simplifying complex legal and banking documents.
    Your task is to rewrite the following legal text in plain language.
    
    **Key Legal Concepts Identified:** {', '.join(embedding_keywords)}
    
    **Simplified Explanation:**
    - Explain the meaning in plain language.
    - Maintain legal accuracy while being concise.
    - Include relevant legal implications if necessary.
    
    **Key Terms Explained (Point-wise): EACH KEY TERM STARTS IN A IN NEW LINE ACCORDING TO HTML FORMAT**
    - Provide short definitions or implications for the key legal terms.
    **Generate an output in html format and make sure that it is left aligned and max heading should be h5 and the heading should speak of the content**
    
    **Original Legal Text:**
    {original_text}
    """
    response = llm.invoke(prompt)
    #Instead of string returning in this format
    return HTMLResponse(content=response.content)
