from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.summarizer_service import generate_summary_from_pdf

router = APIRouter()
from fastapi.responses import HTMLResponse

@router.post("/summarize", summary="Summarize a legal contract PDF", response_class=HTMLResponse)
async def summarize_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    try:
        from io import BytesIO
        file_bytes = await file.read()
        pdf_file = BytesIO(file_bytes)
        
        # Generate an HTML summary instead of a plain string
        summary_html = generate_summary_from_pdf(pdf_file)

        # Ensure FastAPI correctly returns the summary as HTML
        return HTMLResponse(content=summary_html, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
