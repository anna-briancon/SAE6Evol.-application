import json
import random
import requests
import re
from .models import Artist
import string
from typing import Tuple, Any


def get_lyrics(artist, title):
    """
    Call API to get song lyrics

    return lyrics as string
    """
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('lyrics', '')
    return None


def clean_lyrics(lyrics, title):
    """
    Clean lyrics from artist and title

    return cleaned lyrics as string
    """
    pattern = re.compile(r"Paroles de la chanson\s" + re.escape(title) + r"\spar\s.+\n", re.IGNORECASE)
    cleaned_lyrics = re.sub(pattern, '', lyrics)
    return cleaned_lyrics


def clean_lyrics2(lyrics):
    """
    Clean lyrics from artist and title

    return cleaned lyrics as string
    """
    cleaned_lyrics = re.sub(r"Paroles de la chanson .* par .*", "", lyrics)
    return cleaned_lyrics.strip()


def get_words(lyrics: str) -> list[str]:
    """
    Isolate each word of lyrics

    return lyrics as list of string
    """
    #lyrics = format_lyrics(lyrics)
    return lyrics.split('\n')


def get_hidden_lyrics(lyrics: str) -> list[str]:
    """
    Create hidden lyrics

    return hidden lyrics as list of string
    """
    lyrics = format_lyrics(lyrics)
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


def format_lyrics(lyrics: str) -> str:
    """
    Format lyrics

    return formated lyrics as string
    """
    lyrics = lyrics.replace('\r', ' \r').replace('\n', ' \n ').replace("'", "' ").replace(',', ' ,').replace('?',' ?').replace('!', ' !').replace('!', ' !')
    lyrics = lyrics.replace("'", "' ").replace(',', ' ,').replace('?', ' ?').replace('!', ' !').replace('!',' !').replace('(', '( ').replace(')', ' )')
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

def load_artists() -> str:
    """
    Load data from json file to database

    return confirmation message
    """
    json_file = './../artists.json'

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    artists = Artist.objects.all()
    if artists.exists():
        artists.delete()

    for artist in data:
        new_artist = Artist(name=artist['name'], songs=artist['songs'])
        new_artist.save()

    return 'Data loaded successfully.'
# ################
def remove_random_word(lyrics: str) -> (str, str):
    array_of_strings = lyrics.split(' ')

    while True:
        random_index = random.randint(0, len(array_of_strings) - 1)
        random_word = array_of_strings[random_index].strip(string.punctuation)
        if random_word and not all(char in string.punctuation for char in random_word):
            break

        # Replace the selected word with underscores in the original array
    array_of_strings[random_index] = array_of_strings[random_index].replace(random_word, '_' * len(random_word))

    # Transform the surrounding words into a string with whitespace and add <br> every five words
    surrounding_words_string = ''
    for i, word in enumerate(array_of_strings):
        surrounding_words_string += word + ' '

    surrounding_words_string = surrounding_words_string.strip()

    return random_word, surrounding_words_string

def get_hidden_lyrics(lyrics: str) -> list[str]:
    """
    Create hidden lyrics

    return hidden lyrics as list of string
    """
    lyrics = format_lyrics(lyrics)
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
    lyrics = lyrics.replace('\r', ' \r').replace('\n', ' \n ').replace("'", "' ").replace(',', ' ,').replace('?',' ?').replace('!', ' !').replace('!', ' !')
    lyrics = lyrics.replace("'", "' ").replace(',', ' ,').replace('?', ' ?').replace('!', ' !').replace('!',' !').replace('(', '( ').replace(')', ' )')
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
    Get random artist and song from database

    return artist and song as dictionary
    """
    artists = Artist.objects.all()
    if not artists.exists():
        raise ValueError("No artists found in the database")

    while True:
        random_artist = random.choice(artists)

        random_song = random.choice(random_artist.songs)
        lyrics = get_lyrics(random_artist.name, random_song)

        if lyrics:
            cleaned_lyrics = clean_lyrics(lyrics, random_song)

            return {
                'artist': random_artist.name,
                'title': random_song,
                'lyrics': cleaned_lyrics
            }


def load_artists() -> str:
    """
    Load data from json file to database

    return confirmation message
    """
    json_file = './../artists.json'

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    artists = Artist.objects.all()
    if artists.exists():
        artists.delete()

    for artist in data:
        new_artist = Artist(name=artist['name'], songs=artist['songs'])
        new_artist.save()

    return 'Data loaded successfully.'

def process_lyrics(lyrics: str):
    words = lyrics.split()
    processed_lyrics = ['_' * len(word.strip(string.punctuation)) if word.strip(string.punctuation) else word for word in words]
    return words, processed_lyrics

def reveal_word(words, processed_lyrics, guess):
    for i, word in enumerate(words):
        if word.strip(string.punctuation).lower() == guess.lower():
            processed_lyrics[i] = word
    return processed_lyrics