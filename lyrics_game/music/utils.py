import json
import random
import requests
import re
from models import Artist, Song

def get_lyrics(artist: str, song: str) -> str:
    '''
    Call API to get song lyrics

    return lyrics as string
    '''
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', '')
    return None

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
    hidden_lyrics = re.sub(r'[a-zA-Z]','_',lyrics)
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
    fichier_json = './../../chanteurs.json'

    # Lire le fichier JSON
    with open(fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    chanteur_aleatoire = random.choice(data )
    chanteur_modifiee = chanteur_aleatoire['name'].replace(" ", "%")

    # Afficher le contenu du fichier JSON
    chanson_aleatoire = random.choice(chanteur_aleatoire['songs'])
    chaine_modifiee = chanson_aleatoire.replace(" ", "%")
    return get_lyrics(chanteur_modifiee, chaine_modifiee)
    
