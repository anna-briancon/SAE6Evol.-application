import json
import random
import requests

def get_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', '')
    return None

def get_artist():

    fichier_json = './../chanteurs.json'

# Lire le fichier JSON
    with open(fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    chanteur_aleatoire = random.choice(data )
    
    chanteur_modifiee = chanteur_aleatoire['name'].replace(" ", "%")
# Afficher le contenu du fichier JSON
    chanson_aleatoire = random.choice(chanteur_aleatoire['songs'])
    chaine_modifiee = chanson_aleatoire.replace(" ", "%")
    return get_lyrics(chanteur_modifiee, chaine_modifiee)
