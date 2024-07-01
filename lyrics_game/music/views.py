from django.shortcuts import render

def home(request):
    return render(request, 'music/home.html')

def artist_quiz(request):
    return render(request, 'music/artist.html')

def lyrics_quiz(request):
    return render(request, 'music/lyrics.html')