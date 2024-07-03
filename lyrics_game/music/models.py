from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class Artist(models.Model):
    name = models.CharField(max_length=100)
    # string array
    songs = models.JSONField(default=list)

    def __str__(self):
        return self.name + ' - ' + str(len(self.songs)) + ' songs'


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
