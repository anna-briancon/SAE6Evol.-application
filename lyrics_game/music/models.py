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


# artist page
class ArtistPage(Page):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    content_panels = Page.content_panels + [
        FieldPanel('artist')
    ]
