from django.core.management.base import BaseCommand, CommandError
from music.models import Artist


class Command(BaseCommand):
    help = 'Add or remove songs from an artist'

    def add_arguments(self, parser):
        parser.add_argument('artist_id', type=int, help='ID of the artist')
        parser.add_argument('action', type=str, choices=['add', 'remove'], help='Action to perform: add or remove a song')
        parser.add_argument('songs', nargs='+', type=str, help='Songs to add or remove')

    def handle(self, *args, **options):
        artist_id = options['artist_id']
        action = options['action']
        songs = options['songs']

        try:
            artist = Artist.objects.get(pk=artist_id)
        except Artist.DoesNotExist:
            raise CommandError(f"Artist with ID {artist_id} does not exist.")

        if action == 'add':
            self.add_songs(artist, songs)
        elif action == 'remove':
            self.remove_songs(artist, songs)

    def add_songs(self, artist, songs):
        added_songs = []
        existing_songs = []
        for song in songs:
            if song not in artist.songs:
                artist.songs.append(song)
                added_songs.append(song)
            else:
                existing_songs.append(song)

        artist.save()

        if added_songs:
            self.stdout.write(self.style.SUCCESS(f"Songs added successfully: {', '.join(added_songs)}"))
        if existing_songs:
            self.stdout.write(self.style.WARNING(f"Songs already exist: {', '.join(existing_songs)}"))

    def remove_songs(self, artist, songs):
        removed_songs = []
        not_found_songs = []
        for song in songs:
            if song in artist.songs:
                artist.songs.remove(song)
                removed_songs.append(song)
            else:
                not_found_songs.append(song)

        artist.save()

        if removed_songs:
            self.stdout.write(self.style.SUCCESS(f"Songs removed successfully: {', '.join(removed_songs)}"))
        if not_found_songs:
            self.stdout.write(self.style.WARNING(f"Songs not found: {', '.join(not_found_songs)}"))
