from django.shortcuts import render, get_object_or_404
from .forms import LyricsForm
from .models import Song


def home(request):
    return render(request, 'music/home.html')

def artist_quiz(request):
    return render(request, 'music/artist.html')

def lyrics_quiz(request):
    id = 1
    #song = get_object_or_404(Song, id=id)
    #answer = song.answer
    #lyrics = song.lyrics
    tmpLyrics = "Shall I compare thee to a summer's day? Thou art more lovely and more temperate. And summer's lease hath all too short a date."
    tmpAnswer = "summer"
    songWithoutAnswer = tmpLyrics.replace(tmpAnswer, '_____', 1)
    return render(request,
                  'music/complete-lyrics.html', {'lyrics': songWithoutAnswer, 'answer': tmpAnswer})