from django.test import TestCase
from .models import Artist

# tests sur les objets Article
class ArticleTests(TestCase):
    def setUp(self):
        # store 3 articles in test database
        artist = Artist.objects.create(name="The Beatles", songs=["Hey Jude", "Let It Be", "Yesterday"])
        artist2 = Artist.objects.create(name="Elton John", songs=["Rocket Man", "Tiny Dancer", "Your Song"])
        artist3 = Artist.objects.create(name="Maroon 5", songs=["Sugar", "Moves Like Jagger", "She Will Be Loved"])
        
        
    def test_number_articles(self):
        """check that test artists are correctly identified"""
        artists = Artist.objects.filter(name__startswith="The")
        self.assertEqual(artists.count(), 1)

    def test_create_article(self):
        """check that new artiste is correctly stored"""
        Artist.objects.create(name="Dua Lipa", songs=["New Rules", "Don't Start Now", "Levitating"])
        artist = Artist.objects.get(name="Dua Lipa")
        self.assertEqual(artist.songs[0], "New Rules")

    def test_delete_article(self):
        """check that test artists can be correctly deleted"""
        Artist.objects.filter(name__startswith="The").delete() # remove 1 articles from 3
        artists = Artist.objects.all() # 2 article should be remaining
        self.assertEqual(artists.count(), 2)
 
    