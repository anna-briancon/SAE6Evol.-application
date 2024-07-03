import json
import random
import requests
import re
from music.models import Artist, Song

def get_lyrics(artist: str, song: str) -> str:
    '''
    Call API to get song lyrics

    return lyrics as string
    '''
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
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

def clean_lyrics2(lyrics):
    cleaned_lyrics = re.sub(r"Paroles de la chanson .* par .*", "", lyrics)
    return cleaned_lyrics.strip()

def get_words(lyrics: str) -> list[str]:
    '''
    Isolate each word of lyrics

    return lyrics as list of string
    '''
    lyrics = format(lyrics)
    return lyrics.split(' ')

def get_hidden_lyrics(lyrics: str) -> list[str]:
    '''
    Create hidden lyrics

    return hidden lyrics as list of string
    '''
    lyrics = format(lyrics)
    head,hidden_lyrics = lyrics.split('\r',1)
    hidden_lyrics = re.sub(r'[a-zA-Z]','_',hidden_lyrics)
    hidden_lyrics = head + hidden_lyrics
    return hidden_lyrics.split(' ')

def map_mord(split_lyrics : list[str]) -> dict[str,list[int]]:
    '''
    Create dictionary with word as string as key and the index of each iteration of the word

    return dictionary with string as key and list of integer as value
    '''
    lyrics_dict = {}
    for index in range(len(split_lyrics)):
        if split_lyrics[index].lower() != '\r' and  split_lyrics[index].lower() != '\n':
            if split_lyrics[index].lower() in lyrics_dict.keys():
                lyrics_dict[split_lyrics[index].lower()].append(index)
            else:
                lyrics_dict[split_lyrics[index].lower()] = [index]
    return lyrics_dict

def format(lyrics: str) -> str:
    '''
    Format lyrics

    return formated lyrics as string
    '''
    lyrics = lyrics.replace('\r',' \r').replace('\n',' \n ').replace("'","' ").replace(',',' ,').replace('?',' ?').replace('!',' !').replace('!',' !')
    lyrics = lyrics.replace("'","' ").replace(',',' ,').replace('?',' ?').replace('!',' !').replace('!',' !').replace('(','( ').replace(')',' )')
    return lyrics

def is_word_in_lyrics(word: str, dict_lyrics: dict[str,list[int]]) -> None | list[int]:
    '''
    Check if word is in dictionary

    return every index of word or None if not in dictionary
    '''
    if word in dict_lyrics.keys():
        return dict_lyrics[word]
    else:
        return None

def get_artist() -> str:
    '''
    choose a random song

    return song lyrics as string
    '''
    fichier_json = './../chanteurs.json'

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
