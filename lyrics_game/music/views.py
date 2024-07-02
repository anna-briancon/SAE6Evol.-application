# views.py
from django.shortcuts import render
from .models import Chanteur, Chanson
from .utils import get_lyrics, get_artist

def artiste_view(request):
    lyrics = get_artist()  
    context = {'lyrics': lyrics}
    return render(request, 'artiste_page/artiste.html', context)

def guess_artist(request):
    if request.method == 'POST':
        artist_guess = request.POST.get('artist_guess')
        title_guess = request.POST.get('title_guess')

        correct_artist = 'Artiste correct'
        correct_title = 'Titre correct'
        if artist_guess == correct_artist and title_guess == correct_title:
            message = "Bravo, vous avez deviné correctement !"
        else:
            message = "Désolé, ce n'est pas la bonne réponse."

        context = {'message': message}
        return render(request, 'artiste_page/result.html', context)

    return render(request, 'artiste_page/artiste.html')
