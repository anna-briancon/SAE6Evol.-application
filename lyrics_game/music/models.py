from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    lyrics = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.artist.name}"


class ArtistPage(Page):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    content_panels = Page.content_panels + [
        FieldPanel('artist')
    ]

class HomePage(Page):
    game = models.CharField(max_length=100)
    button1 = models.CharField(max_length=100)
    button2 = models.CharField(max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel('game'),
        FieldPanel('button1'),
        FieldPanel('button2')
    ]

class ArtistePage(Page):
    api_url = models.URLField(blank=True)

from django.db import models

class Chanteur(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chanson(models.Model):
    artist = models.ForeignKey(Chanteur, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    lyrics = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.artist}"
