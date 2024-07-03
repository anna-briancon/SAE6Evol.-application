from django.urls import path
from . import views
from .views import artiste_view

urlpatterns = [
    path('artiste/', views.artiste_view, name='artiste'),
    path('guess/', views.guess_artist, name='guess_artist'),
    path('get_hint/', views.get_hint, name='get_hint'),

]
