from django.urls import path
from . import views
from .views import artiste_view

urlpatterns = [
    path('artiste/', views.artiste_view, name='artiste'),
    path('guess/', views.guess_artist, name='guess_artist'),
    path('get_hint/', views.get_hint, name='get_hint'),
    path('titre/', views.titre_view, name='titre'),
    path('guess_title/', views.guess_title, name='guess_title'),
    path('get_hint_title/', views.get_hint_title, name='get_hint_title'),
]
