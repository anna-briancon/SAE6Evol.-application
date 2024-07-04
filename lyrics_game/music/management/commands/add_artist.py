from django.core.management.base import BaseCommand, CommandError
from music.models import Artist


class Command(BaseCommand):
    help = 'Add a new artist with songs to the database'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the artist')
        parser.add_argument('songs', nargs='+', type=str, help='List of songs')

    def handle(self, *args, **options):
        name = options['name']
        songs = options['songs']

        if Artist.objects.filter(name=name).exists():
            raise CommandError(f"An artist with the name '{name}' already exists.")

        artist = Artist(name=name, songs=songs)
        artist.save()

        self.stdout.write(self.style.SUCCESS(f"Artist '{name}' with songs {', '.join(songs)} added successfully."))

