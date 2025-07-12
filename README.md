# M1 - Brief 1 Exposition du Modèle via API, Journalisation et Conteneurisation

---

Récupérer les librairies nécessaires au fonctionnement du projet:

```bash
pip install -r requirements.txt
```

On construit l'image Docker:

```bash 
docker build -t sentiment-api .
```

On lance le conteneur à partir de l'image :

```bash
docker run -d -p 5000:5000 --name sentiment-api-container sentiment-api
```

Vérifier ensuite si le service est ok via l'url :
http://localhost:5000/health

Lancer ensuite l'interface streamlit:
```bash
streamlit run sentiment_app.py 
```