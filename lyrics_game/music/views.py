from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_artist

def artiste_view(request):
    artist_data = get_artist()  
    context = {
        'lyrics': artist_data['lyrics'],
        'correct_artist': artist_data['artist'],
        'correct_title': artist_data['title']
    }
    return render(request, 'artiste_page/artiste.html', context)

def guess_artist(request):
    if request.method == 'POST':
        artist_guess = request.POST.get('artist_guess')
        title_guess = request.POST.get('title_guess')

        correct_artist = request.POST.get('correct_artist')
        correct_title = request.POST.get('correct_title')
        
        if artist_guess == correct_artist and title_guess == correct_title:
            message = "Bravo, vous avez deviné correctement !"
        else:
            message = "Désolé, ce n'est pas la bonne réponse."

        return JsonResponse({'message': message})

    return JsonResponse({'message': 'Invalid request'}, status=400)
