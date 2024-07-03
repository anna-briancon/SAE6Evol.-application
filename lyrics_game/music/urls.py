from django.urls import path
from . import views


urlpatterns = [
    path('artiste/', views.artiste_view, name='artiste'),
    path('guess/', views.guess_artist, name='guess_artist'),
]
