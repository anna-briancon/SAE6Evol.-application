from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/', views.artist_quiz, name='artist'),
    path('lyrics/', views.lyrics_quiz, name='lyrics'),
]