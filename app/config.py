from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = "llama3"
    persist_dir: str = "data/vectordb"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

settings = Settings()
