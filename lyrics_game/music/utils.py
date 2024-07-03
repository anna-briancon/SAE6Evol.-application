import json
import random
from typing import Tuple, Any

import requests
import re
import string
from .models import Artist, Song


def get_lyrics(artist: str, song: str) -> str:
    """
    Call API to get song lyrics

    return lyrics as string
    """
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', '')
    return None


def get_words(lyrics: str) -> list[str]:
    """
    Isolate each word of lyrics

    return lyrics as list of string
    """
    lyrics = format(lyrics)
    return lyrics.split(' ')

def is_valid_string(s):
    special_characters = string.punctuation + string.whitespace
    return s and not all(char in special_characters for char in s)


def remove_random_word(lyrics: str) -> (str, str):
    array_of_strings = lyrics.split(' ')

    while True:
        random_index = random.randint(0, len(array_of_strings) - 1)
        random_word = array_of_strings[random_index].strip(string.punctuation)
        if random_word and not all(char in string.punctuation for char in random_word):
            break

        # Replace the selected word with underscores in the original array
    array_of_strings[random_index] = array_of_strings[random_index].replace(random_word, '_' * len(random_word))

    # Get 15 words before and after the selected word
    start_index = max(0, random_index - 15)
    end_index = min(len(array_of_strings), random_index + 16)
    surrounding_words_with_special_chars = array_of_strings[start_index:end_index]

    # Transform the surrounding words into a string with whitespace and add <br> every five words
    surrounding_words_string = ''
    for i, word in enumerate(surrounding_words_with_special_chars):
        if i > 0 and i % 5 == 0:
            surrounding_words_string += '<br>'
        surrounding_words_string += word + ' '

    surrounding_words_string = surrounding_words_string.strip()

    return random_word, surrounding_words_string

def get_hidden_lyrics(lyrics: str) -> list[str]:
    """
    Create hidden lyrics

    return hidden lyrics as list of string
    """
    lyrics = format(lyrics)
    hidden_lyrics = re.sub(r'[a-zA-Z]', '_', lyrics)
    return hidden_lyrics.split(' ')


def map_mord(split_lyrics: list[str]) -> dict[str, list[int]]:
    """
    Create dictionary with word as string as key and the index of each iteration of the word

    return dictionary with string as key and list of integer as value
    """
    lyrics_dict = {}
    for index in range(len(split_lyrics)):
        if split_lyrics[index].lower() != '\r' and split_lyrics[index].lower() != '\n':
            if split_lyrics[index].lower() in lyrics_dict.keys():
                lyrics_dict[split_lyrics[index].lower()].append(index)
            else:
                lyrics_dict[split_lyrics[index].lower()] = [index]
    return lyrics_dict


def format(lyrics: str) -> str:
    """
    Format lyrics

    return formated lyrics as string
    """
    lyrics = lyrics.replace('\r', ' \r').replace('\n', ' \n ').replace("'", "' ").replace(',', ' ,').replace('?',
                                                                                                             ' ?').replace(
        '!', ' !').replace('!', ' !')
    lyrics = lyrics.replace("'", "' ").replace(',', ' ,').replace('?', ' ?').replace('!', ' !').replace('!',
                                                                                                        ' !').replace(
        '(', '( ').replace(')', ' )')
    return lyrics


def is_word_in_lyrics(word: str, dict_lyrics: dict[str, list[int]]) -> None | list[int]:
    """
    Check if word is in dictionary

    return every index of word or None if not in dictionary
    """
    if word in dict_lyrics.keys():
        return dict_lyrics[word]
    else:
        return None

def get_artist() -> tuple[str, Any, Any]:
    """
    choose a random song

    return song lyrics as string
    """
    fichier_json = './../chanteurs.json'

    # Lire le fichier JSON
    with open(fichier_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    chanteur_aleatoire = random.choice(data)
    chanteur_modifiee = chanteur_aleatoire['name'].replace(" ", "%")
    chanteur_aleatoire_name = chanteur_aleatoire['name']
    # Afficher le contenu du fichier JSON
    chanson_aleatoire = random.choice(chanteur_aleatoire['songs'])
    chaine_modifiee = chanson_aleatoire.replace(" ", "%")
    return get_lyrics(chanteur_modifiee, chaine_modifiee), chanteur_aleatoire_name, chanson_aleatoire


def process_lyrics(lyrics: str):
    words = lyrics.split()
    processed_lyrics = ['_' * len(word.strip(string.punctuation)) if word.strip(string.punctuation) else word for word in words]
    print("coucou")
    return words, processed_lyrics

def reveal_word(words, processed_lyrics, guess):
    for i, word in enumerate(words):
        if word.strip(string.punctuation).lower() == guess.lower():
            processed_lyrics[i] = word
    return processed_lyrics