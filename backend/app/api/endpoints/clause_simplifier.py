from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.clause_simplifier_service import (
    get_batch_legal_embeddings,
    extract_keywords_from_embedding,
    extract_legal_keywords,
    simplify_legal_text_using_embeddings
)
import numpy as np

router = APIRouter()

class ClauseSimplifierRequest(BaseModel):
    text: str

@router.post("/clause-simplify", summary="Simplify a selected legal clause")
def clause_simplify(request: ClauseSimplifierRequest):
    clause_text = request.text
    if not clause_text:
        raise HTTPException(status_code=400, detail="Text is required.")
    try:
        legal_embedding = get_batch_legal_embeddings([clause_text])[0]
        reference_terms = ["loan default", "interest rate", "foreclosure", "contract breach", "legal obligations"]
        extracted_keywords = extract_keywords_from_embedding(legal_embedding, reference_terms, clause_text)
        ner_keywords = extract_legal_keywords(clause_text)
        print(ner_keywords)
        print(extracted_keywords)
        all_keywords = list(set(extracted_keywords + ner_keywords))
        simplified_text = simplify_legal_text_using_embeddings(all_keywords, clause_text)
        return {"simplified_text": simplified_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
