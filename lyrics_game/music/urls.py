from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/', views.artist_quiz, name='artist'),
    path('lyrics/', views.lyrics_quiz, name='lyrics'),
    path('lyrics-game/', views.lyrics_game_view, name='lyrics_game'),

    path('artiste/', views.artiste_view, name='artiste'),
    path('guess/', views.guess_artist, name='guess_artist'),
    path('get_hint/', views.get_hint, name='get_hint'),

    path('titre/', views.titre_view, name='titre'),
    path('guess_title/', views.guess_title, name='guess_title'),
    path('get_hint_title/', views.get_hint_title, name='get_hint_title'),

    path('juste_artiste/', views.juste_artiste_view, name='juste_artiste'),
    path('guess_juste_artiste/', views.guess_juste_artiste, name='guess_juste_artiste'),
    path('get_hint_juste_artiste/', views.get_hint_juste_artiste, name='get_hint_juste_artiste'),
]
