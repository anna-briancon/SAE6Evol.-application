import django_filters

from music.models import Artist


class ArtistFilter(django_filters.FilterSet):
    class Meta:
        model = Artist
        fields = ['name']
