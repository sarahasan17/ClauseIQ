import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    LLAMA_PARSER_API_KEY: str = os.getenv("LLAMA_PARSER_API_KEY")
    HUGGINGFACE_TOKEN: str = os.getenv("HUGGINGFACE_TOKEN")

settings = Settings()
