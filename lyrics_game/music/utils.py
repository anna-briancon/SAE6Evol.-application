import json
import random
import requests
import re

from .models import Artist


def get_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', '')
    return None


def clean_lyrics(lyrics, title):
    pattern = re.compile(r"Paroles de la chanson\s" + re.escape(title) + r"\spar\s.+\n", re.IGNORECASE)
    cleaned_lyrics = re.sub(pattern, '', lyrics)
    return cleaned_lyrics


def get_artist():
    fichier_json = './../artists.json'

    with open(fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    while True:
        chanteur_aleatoire = random.choice(data)
        chanteur_modifiee = chanteur_aleatoire['name'].replace(" ", "%")
        chanson_aleatoire = random.choice(chanteur_aleatoire['songs'])
        chaine_modifiee = chanson_aleatoire.replace(" ", "%")

        lyrics = get_lyrics(chanteur_modifiee, chaine_modifiee)
        if lyrics:
            cleaned_lyrics = clean_lyrics(lyrics, chanson_aleatoire)
            return {
                'artist': chanteur_aleatoire['name'],
                'title': chanson_aleatoire,
                'lyrics': cleaned_lyrics
            }


def load_artists():
    json_file = './../artists.json'

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for artist in data:
        new_artist = Artist(name=artist['name'], songs=artist['songs'])
        new_artist.save()

    return 'Data loaded successfully.'
