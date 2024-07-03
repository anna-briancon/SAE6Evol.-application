from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    lyrics = models.TextField()
    answer = models.CharField(max_length=200, blank=True)
    # string array
    songs = models.JSONField(default=list)

    def __str__(self):
        return self.name, ' - ', self.songs, ' songs'


class ArtistPage(Page):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    content_panels = Page.content_panels + [
        FieldPanel('artist')
    ]


class HomePage(Page):
    buttonGuessTitle = models.CharField(max_length=100, blank=True)
    buttonGuessArtist = models.CharField(max_length=100, blank=True)
    buttonGuessLyrics = models.CharField(max_length=100, blank=True)
    buttonGuessTitleAndArtist = models.CharField(max_length=100, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('buttonGuessTitle'),
        FieldPanel('buttonGuessArtist'),
        FieldPanel('buttonGuessLyrics'),
        FieldPanel('buttonGuessTitleAndArtist')
    ]
