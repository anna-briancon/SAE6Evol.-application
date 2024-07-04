from django.core.management.base import BaseCommand, CommandError
from music.models import Artist


class Command(BaseCommand):
    help = 'Delete an artist from the database'

    def add_arguments(self, parser):
        parser.add_argument('artist_id', type=int, help='ID of the artist to delete')

    def handle(self, *args, **options):
        artist_id = options['artist_id']

        try:
            artist = Artist.objects.get(pk=artist_id)
            artist_name = artist.name
            artist.delete()
            self.stdout.write(self.style.SUCCESS(f"Artist '{artist_name}' with ID {artist_id} deleted successfully."))
        except Artist.DoesNotExist:
            raise CommandError(f"Artist with ID {artist_id} does not exist.")
