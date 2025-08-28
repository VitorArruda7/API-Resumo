import os

class Settings:
    # Define modelo padrão (pode ser sobrescrito no .env ou Docker)
    MODEL_NAME: str = os.getenv("MODEL_NAME", "facebook/bart-large-cnn")

settings = Settings()