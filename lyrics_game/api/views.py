from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import ArtistFilter
from music.models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter

    @action(detail=True, methods=['patch'])
    def add_song(self, request, pk=None):
        artist = self.get_object()
        new_songs = request.data.get('songs', [])

        if isinstance(new_songs, list):
            for song in new_songs:
                if song not in artist.songs:
                    artist.songs.append(song)
                else:
                    return Response({"detail": f"Song '{song}' already exists."}, status=status.HTTP_400_BAD_REQUEST)
            artist.save()
            return Response({"detail": "Songs added successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Songs must be a list."}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def remove_song(self, request, pk=None):
        artist = self.get_object()
        song_to_remove = request.data.get('song', None)

        if song_to_remove is None:
            return Response({"detail": "Please provide 'song' in request body."}, status=status.HTTP_400_BAD_REQUEST)

        if song_to_remove in artist.songs:
            artist.songs.remove(song_to_remove)
            artist.save()
            return Response({"detail": f"Song '{song_to_remove}' removed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"Song '{song_to_remove}' not found in artist's songs."}, status=status.HTTP_400_BAD_REQUEST)

