import requests
import re
from models import Artist, Song

def get_lyrics(artist: Artist, song: Song) -> str:
    '''
    Call API to get song lyrics

    return lyrics as string
    '''
    url = f"https://api.lyrics.ovh/v1/{artist.name}/{song.title}"
    response = requests.get(url)
    if response.status_code == 200:
        song.lyrics = response.json().get('lyrics', '')
        return song.lyrics
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
