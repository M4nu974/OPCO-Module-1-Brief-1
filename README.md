# M1 - Brief 1 Exposition du Modèle via API, Journalisation et Conteneurisation

---

# Documentation de l’API d’Analyse de Sentiment

## 1. Architecture de l’API

- **Framework principal** : FastAPI, pour une API web rapide, asynchrone et bien documentée.
- **Analyse de sentiment** : Utilisation de `SentimentIntensityAnalyzer` de NLTK (modèle VADER) pour analyser le texte.
- **Validation des données** : Modèles Pydantic pour assurer la validité des entrées JSON reçues.
- **Modularité** : Séparation entre la logique API (analyse de sentiment dans `sentiment_api.py`) et l’interface utilisateur (Streamlit dans `sentiment_streamlit.py`).
- **Journalisation** : Intégration de `loguru` pour tracer les requêtes, réponses, et erreurs dans des fichiers dédiés sous `logs/`.
- **Conteneurisation** : Dockerfile permettant de packager l’API dans un conteneur.

## 2. Routes disponibles

| Route       | Méthode | Description                                                   | Entrée                          | Sortie                                   |
|-------------|---------|---------------------------------------------------------------|--------------------------------|------------------------------------------|
| `/predict/` | POST    | Analyse le sentiment d’un texte donné                         | JSON `{ "texte": "votre texte" }` | JSON avec scores `{neg, neu, pos, compound}` |
| `/health`   | GET     | Vérifie l’état de santé du service                            | Aucune                         | JSON `{ "status": "ok", "message": "Service is healthy" }` |

- La route `/predict/` utilise le modèle Pydantic `Texte` pour valider que le champ `texte` est bien une chaîne de caractères.
- La route `/health` permet un monitoring simple pour vérifier que l’API est opérationnelle.

## 3. Système de logs

- **Bibliothèque utilisée** : `loguru` pour une journalisation simple, performante et flexible.
- **Fichiers de logs** :
    - `logs/sentiment_api.log` : journalise les requêtes reçues, résultats d’analyse, et erreurs côté API.
    - `logs/sentiment_streamlit.log` : journalise les entrées utilisateur, résultats reçus de l’API, et erreurs côté interface Streamlit.
- **Configuration** :
    - Rotation automatique des fichiers de logs (par exemple tous les 10 MB).
    - Création automatique du dossier `logs/` si inexistant.

## 4. Procédures de test

- **Test de l’API** :
    - Utiliser `curl` ou Postman pour envoyer des requêtes POST à `/predict/` avec différents textes.
    - Vérifier que la réponse contient bien les scores de sentiment.
    - Tester la route `/health` avec une requête GET pour s’assurer que le service répond.
- **Test de l’interface Streamlit** :
    - Saisir du texte dans la zone prévue.
    - Cliquer sur "Analyser" et vérifier que les résultats s’affichent correctement.
    - Observer les logs pour vérifier la bonne journalisation.


---
# Déploiement de l'application :
Préparer un environnement virtuel python avec venv ou conda

Récupérer les librairies nécessaires au fonctionnement du projet:

```bash
pip install -r requirements.txt
```
## Lancer l'API en local :

```bash 
uvicorn sentiment_api:app --port 5000
```

## Ou lancer l'API avec Docker:

On construit l'image Docker:

```bash 
docker build -t sentiment-api .
```

Lancer le conteneur à partir de l'image :

```bash
docker run -d -p 5000:5000 --name sentiment-api-container sentiment-api
```

Vérifier ensuite si le service est ok via l'url :
http://localhost:5000/health

Lancer ensuite l'interface streamlit:
```bash
streamlit run sentiment_app.py 
```