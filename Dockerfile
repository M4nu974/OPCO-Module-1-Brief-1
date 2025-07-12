# Utiliser une image officielle Python légère
FROM python:3.11-slim

# Créer et se placer dans le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt et le code source API
COPY requirements.txt .
COPY sentiment_api.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Télécharger les ressources NLTK nécessaires
RUN python -m nltk.downloader vader_lexicon

# Créer le dossier logs (optionnel, mais recommandé)
RUN mkdir -p logs

# Exposer le port sur lequel Uvicorn va écouter
EXPOSE 5000

# Commande pour lancer l'API avec reload désactivé (production)
CMD ["uvicorn", "sentiment_api:app", "--host", "0.0.0.0", "--port", "5000"]
