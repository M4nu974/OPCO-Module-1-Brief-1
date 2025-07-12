from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer
from loguru import logger

import os

# Création du dossier logs s'il n'existe pas
os.makedirs("logs", exist_ok=True)
logger.add("logs/sentiment_api.log", rotation="10 MB")

app = FastAPI()
sia = SentimentIntensityAnalyzer()

class Texte(BaseModel):
    texte: str

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Le service est opérationnel"}

@app.post("/predict/")
async def predict(data: Texte):
    logger.info(f"Analyse du texte: {data.texte}")
    try:
        logger.info(f"Texte reçu: {data.texte}")
        scores = sia.polarity_scores(data.texte)
        logger.info(f"Scores: {scores}")
        return scores
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {e}")
        return {"error": str(e)}
