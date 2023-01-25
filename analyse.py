"""
Ce script analyse le text d'un fichier en utilisant NLP
Auteur: Mohamad
Créer le: 2024-01-25
"""
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

json_file = "json_files_dir/qatar219.json"

with open(json_file,'r') as f:
    tweets = json.load(f)

json_file = 'twitter_data.json'
batch_size = 100 # Taille du lot à traiter pour pouvoir traiter une grande quantité d'info

# Initialisation de l'analyseur de sentiments
sia = SentimentIntensityAnalyzer()


# Initialisation du dictionnaire de résultats
results = {}

# Boucle de traitement par lot
batch_count = 0
i = 0
for num,tweet in tweets['Text'].items():
    print(i*100//len(tweets["Text"].values()),"%") # Affichage de l'évolution du script
    i+=1
    # Analyse de la polarité
    polarity = TextBlob(tweet).sentiment.polarity
    # Analyse de la subjectivité
    subjectivity = TextBlob(tweet).sentiment.subjectivity
    # Analyse des sentiments
    sentiment = sia.polarity_scores(tweet)['compound']
    # Ajout des résultats au dictionnaire
    results[tweets["TweetId"].get(num)] = {'polarity': polarity, 'subjectivity': subjectivity, 'sentiment': sentiment}
    batch_count += 1
    if batch_count >= batch_size:
        # Conversion des résultats en json et enregistrement dans le fichier
        with open(json_file, 'a') as f:
            json.dump(results, f)
        # Réinitialisation du dictionnaire de résultats
        results = {}
        batch_count = 0

# Enregistrement des résultats restants dans le fichier json
with open(json_file, 'a') as f:
    json.dump(results, f)

print('Analyse terminée avec succès !')