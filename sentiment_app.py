import streamlit as st
import requests
from loguru import logger
import os

API_URL = "http://127.0.0.1:5000"
os.makedirs("logs", exist_ok=True)
logger.add("logs/sentiment_streamlit.log", rotation="10 MB")

st.title("Analyse de Sentiment")

texte = st.text_area("Entrez votre texte ici :")

if st.button("Analyser"):
    if texte.strip():
        try:
            logger.info(f"Texte utilisateur: {texte}")
            response = requests.post(API_URL+"/predict/", json={"texte": texte})
            response.raise_for_status()
            sentiment = response.json()
            logger.info(f"Résultat API: {sentiment}")
            st.json(sentiment)
            if sentiment['compound'] >= 0.05 :
                st.write("Sentiment global : Positif 😀")
            elif sentiment['compound'] <= -0.05 :
                st.write("Sentiment global : Négatif 🙁")
            else :
                st.write("Sentiment global : Neutre 😐")
            logger.info(f"Résultats affichés: {sentiment}")
        # traitement de la réponse
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur de connexion à l'API : {e}")
        except Exception as e :
            st.error(f"Une erreur est survenue: {e}")
            logger.error(f"Une erreur est survenue: {e}")
    else:
        st.warning("Veuillez saisir un texte.")
