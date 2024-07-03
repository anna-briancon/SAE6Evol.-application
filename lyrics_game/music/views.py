from django.shortcuts import render, get_object_or_404
from .forms import LyricsForm, LyricsGameForm
from .models import Song
from .utils import get_artist, remove_random_word, process_lyrics, reveal_word


def home(request):
    return render(request, 'music/home.html')


def artist_quiz(request):
    return render(request, 'music/artist.html')


def lyrics_quiz(request):
    while True:
        lyrics, singer, song_name = get_artist()
        if lyrics is not None and len(lyrics) > 0:
            break

    if request.method == 'POST':
        form = LyricsForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            answer = form.cleaned_data['random_word']
            if user_input.strip().lower() == answer.lower():
                result = 'Correct!'
                result_color = 'green'
            else:
                result = 'Try again!'
                result_color = 'red'
            words_around = form.cleaned_data['words_around']
        else:
            result = ''
            result_color = ''
            words_around = ""
            answer = ""
    else:
        answer, words_around = remove_random_word(lyrics)
        form = LyricsForm(initial={'random_word': answer, 'words_around': words_around})
        result = ''
        result_color = ''

    return render(request, 'music/complete-lyrics.html', {
        'form': form,
        'lyrics': words_around,
        'result': result,
        'result_color': result_color,
        'answer': answer,
        'singer': singer,
        'song_name': song_name
    })


from django.shortcuts import render, redirect
from .utils import process_lyrics, reveal_word
from .forms import LyricsForm

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
            lyrics, singer, song_name = get_artist()  # This function should fetch the song lyrics
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
            print("hello")
            guess = form.cleaned_data['user_input']
            processed_lyrics = reveal_word(words, processed_lyrics, guess)
            request.session['processed_lyrics'] = processed_lyrics
            if '_' not in processed_lyrics:
                win = True
    else:
        form = LyricsGameForm()
    print(lyrics)
    context = {
        'form': form,
        'processed_lyrics': ' '.join(processed_lyrics),
        'singer': singer,
        'song_name': song_name,
        'win': win
    }
    return render(request, 'music/lyrics_game.html', context)



