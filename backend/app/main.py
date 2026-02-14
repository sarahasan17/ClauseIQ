from fastapi import FastAPI
from app.api.endpoints import summarizer, clause_simplifier
# from api.endpoints import summarizer, clause_simplifier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Legal Contract Simplifier API")

# Configure CORS for Angular frontend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(summarizer.router, prefix="/api", tags=["Summarizer"])
app.include_router(clause_simplifier.router, prefix="/api", tags=["Clause Simplifier"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Legal Contract Simplifier API!"}
