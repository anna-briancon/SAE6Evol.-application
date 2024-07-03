from django.core.management.base import BaseCommand

from music.utils import load_artists


class Command(BaseCommand):
    help = 'Load data from json file to database'

    def handle(self, *args, **kwargs):
        self.stdout.write(load_artists())
