from django.test import TestCase  
from rest_framework import status
from music.models import Artist
from api.serializers import ArtistSerializer

# tests sur les objets Artist
class ArtistTests(TestCase):
    def setUp(self):
        # store 3 Artists in test database
        artist = Artist.objects.create(name="The Beatles", songs=["Hey Jude", "Let It Be", "Yesterday"])
        artist2 = Artist.objects.create(name="Elton John", songs=["Rocket Man", "Tiny Dancer", "Your Song"])
        artist3 = Artist.objects.create(name="Maroon 5", songs=["Sugar", "Moves Like Jagger", "She Will Be Loved"])
        
        
    def test_number_Artists(self):
        """check that test artists are correctly identified"""
        artists = Artist.objects.filter(name__startswith="The")
        self.assertEqual(artists.count(), 1)

    def test_create_Artist(self):
        """check that new artiste is correctly stored"""
        Artist.objects.create(name="Dua Lipa", songs=["New Rules", "Don't Start Now", "Levitating"])
        artist = Artist.objects.get(name="Dua Lipa")
        self.assertEqual(artist.songs[0], "New Rules")

    def test_delete_Artist(self):
        """check that test artists can be correctly deleted"""
        Artist.objects.filter(name__startswith="The").delete() # remove 1 Artists from 3
        artists = Artist.objects.all() # 2 Artist should be remaining
        self.assertEqual(artists.count(), 2)
        
    


class RESTArtistTests(TestCase):
    
    def setUp(self):
        artist = Artist.objects.create(name="The Beatles", songs=["Hey Jude", "Let It Be", "Yesterday"])
        artist2 = Artist.objects.create(name="Elton John", songs=["Rocket Man", "Tiny Dancer", "Your Song"])
        artist3 = Artist.objects.create(name="Maroon 5", songs=["Sugar", "Moves Like Jagger", "She Will Be Loved"])

    
    def test_get_all_artist(self):
        response = self.client.get('/api/artist/')
        artists = Artist.objects.all().order_by('name')
        serializer_data = ArtistSerializer(artists, many=True).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_get_artist(self):
        response = self.client.get('/rest/artist/?name=The%Beatles')
        artist = Artist.objects.get(name="The Beatles")
        serializer_data = ArtistSerializer(artist).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=None)
    
    def test_add_song(self):
        data = {
            "name": "Squeezie",
            "songs": ["Time time", "Top 1", "Ce petit coté Kawai"]
        }
        response = self.client.patch('/api/artist/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       
    
    def test_add_song_with_artist_created(self):
        data = {
            "songs": ["Time time", "Top 1", "Ce petit coté Kawai"]
        }
        response = self.client.patch('/api/artist/1/add_song')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
 
    def test_remove_song(self):
        data = {
            "songs": "Let It Be"
        }
        response = self.client.patch("/api/artist/1/remove_song/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_remove_artist(self):
        response = self.client.delete("api/artist/2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    