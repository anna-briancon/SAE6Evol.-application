# views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .utils import get_artist, clean_lyrics2, get_words
from .utils import get_artist, remove_random_word, process_lyrics, reveal_word
from .forms import LyricsForm, LyricsGameForm
old_singer =""
old_song_name = ""

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

def lyrics_quiz(request):
    global old_singer
    global old_song_name
    while True:
        information = get_artist()
        lyrics = information['lyrics']
        singer = information['artist']
        song_name = information['title']
        if lyrics is not None and len(lyrics) > 0:
            break

    if request.method == 'POST':
        form = LyricsForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            answer = form.cleaned_data['random_word']
            if user_input.strip().lower() == answer.lower():
                result = 'Bravo, vous avez deviné correctement !'
                result_color = 'green'
            else:
                result = "Désolé, ce n'est pas la bonne réponse."
                result_color = 'red'
            words_around = form.cleaned_data['words_around']
            singer = old_singer
            song_name = old_song_name
        else:
            result = ''
            result_color = ''
            words_around = ""
            answer = ""
    else:
        old_singer = singer
        old_song_name = song_name
        answer, words_around = remove_random_word(lyrics)
        form = LyricsForm(initial={'random_word': answer, 'words_around': words_around})
        result = ''
        result_color = ''

    return render(request, 'page/complete_lyrics.html', {
        'form': form,
        'lyrics': words_around,
        'result': result,
        'result_color': result_color,
        'answer': answer,
        'singer': singer,
        'song_name': song_name
    })

def lyrics_game_view(request):
    if 'change_song' in request.POST:
        if 'song' in request.session:
            del request.session['song']
            del request.session['words']
            del request.session['processed_lyrics']
        return redirect('lyrics_game')
    singer = None
    song_name = None
    lyrics = None
    if 'song' not in request.session:
        while lyrics is None:
            information = get_artist()
            lyrics = information['lyrics']
            singer = information['artist']
            song_name = information['title'] # This function should fetch the song lyrics
        request.session['song'] = lyrics
        words, processed_lyrics = process_lyrics(lyrics)
        request.session['words'] = words
        request.session['processed_lyrics'] = processed_lyrics
        request.session['singer'] = singer
        request.session['song_name'] = song_name
    else:
        lyrics = request.session['song']
        singer = request.session['singer'] if 'singer' in request.session else None
        song_name = request.session['song_name'] if 'song_name' in request.session else None
        words = request.session['words']
        processed_lyrics = request.session['processed_lyrics']
    win = False
    if request.method == 'POST':
        form = LyricsGameForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data['user_input']
            processed_lyrics = reveal_word(words, processed_lyrics, guess)
            request.session['processed_lyrics'] = processed_lyrics
            if '_' not in processed_lyrics:
                win = True
    else:
        form = LyricsGameForm()
    context = {
        'form': form,
        'processed_lyrics': ' '.join(processed_lyrics),
        'singer': singer,
        'song_name': song_name,
        'win': win
    }
    return render(request, 'page/lyrics_game.html', context)