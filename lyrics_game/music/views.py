# views.py

from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_artist, clean_lyrics2, get_words

def artiste_view(request):
    artist_data = get_artist()
    cleaned_lyrics = clean_lyrics2(artist_data['lyrics'])
    cleaned_lyrics = get_words(cleaned_lyrics)
    context = {
        'lyrics': cleaned_lyrics,
        'correct_artist': artist_data['artist'],
        'correct_title': artist_data['title']
    }
    return render(request, 'page/artiste.html', context)

def guess_artist(request):
    if request.method == 'POST':
        artist_guess = request.POST.get('artist_guess').strip().lower()
        title_guess = request.POST.get('title_guess').strip().lower()

        correct_artist = request.POST.get('correct_artist').strip().lower()
        correct_title = request.POST.get('correct_title').strip().lower()
        
        if artist_guess == correct_artist and title_guess == correct_title:
            message = "Bravo, vous avez deviné correctement !"
        else:
            message = "Désolé, ce n'est pas la bonne réponse."

        return JsonResponse({'message': message})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def get_hint(request):
    if request.method == 'GET':
        correct_artist = request.GET.get('correct_artist')
        correct_title = request.GET.get('correct_title')
        hint_type = request.GET.get('hint_type')
        hint_index = int(request.GET.get('hint_index', 0))
        
        if hint_type == 'artist':
            if hint_index < len(correct_artist):
                hint = correct_artist[:hint_index + 1]
                hint_index += 1
            else:
                hint = "Aucun autre indice disponible."
                hint_index = len(correct_artist)
        elif hint_type == 'title':
            if hint_index < len(correct_title):
                hint = correct_title[:hint_index + 1]
                hint_index += 1
            else:
                hint = "Aucun autre indice disponible."
                hint_index = len(correct_title)
        
        return JsonResponse({'hint': hint, 'hint_index': hint_index})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def titre_view(request):
    artist_data = get_artist()
    cleaned_lyrics = clean_lyrics2(artist_data['lyrics'])
    cleaned_lyrics = get_words(cleaned_lyrics)
    context = {
        'lyrics': cleaned_lyrics,
        'correct_artist': artist_data['artist'],
        'correct_title': artist_data['title']
    }
    return render(request, 'page/titre.html', context)

def guess_title(request):
    if request.method == 'POST':
        title_guess = request.POST.get('title_guess').strip().lower()

        correct_title = request.POST.get('correct_title').strip().lower()
        
        if title_guess == correct_title:
            message = "Bravo, vous avez deviné correctement !"
        else:
            message = "Désolé, ce n'est pas la bonne réponse."

        return JsonResponse({'message': message})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def get_hint_title(request):
    if request.method == 'GET':
        correct_title = request.GET.get('correct_title')
        hint_type = request.GET.get('hint_type')
        hint_index = int(request.GET.get('hint_index', 0))
        
        if hint_type == 'title':
            if hint_index < len(correct_title):
                hint = correct_title[:hint_index + 1]
                hint_index += 1
            else:
                hint = "Aucun autre indice disponible."
                hint_index = len(correct_title)
        
        return JsonResponse({'hint': hint, 'hint_index': hint_index})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def juste_artiste_view(request):
    artist_data = get_artist()
    cleaned_lyrics = clean_lyrics2(artist_data['lyrics'])
    cleaned_lyrics = get_words(cleaned_lyrics)

    context = {
        'lyrics': cleaned_lyrics,
        'correct_artist': artist_data['artist'],
        'correct_title': artist_data['title']
    }
    return render(request, 'page/juste_artiste.html', context)

def guess_juste_artiste(request):
    if request.method == 'POST':
        artist_guess = request.POST.get('artist_guess').strip().lower()

        correct_artist = request.POST.get('correct_artist').strip().lower()
        
        if artist_guess == correct_artist:
            message = "Bravo, vous avez deviné correctement !"
        else:
            message = "Désolé, ce n'est pas la bonne réponse."

        return JsonResponse({'message': message})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def get_hint_juste_artiste(request):
    if request.method == 'GET':
        correct_artist = request.GET.get('correct_artist')
        hint_type = request.GET.get('hint_type')
        hint_index = int(request.GET.get('hint_index', 0))
        
        if hint_type == 'artist':
            if hint_index < len(correct_artist):
                hint = correct_artist[:hint_index + 1]
                hint_index += 1
            else:
                hint = "Aucun autre indice disponible."
                hint_index = len(correct_artist)
        
        return JsonResponse({'hint': hint, 'hint_index': hint_index})

    return JsonResponse({'message': 'Invalid request'}, status=400)