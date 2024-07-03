# SAE6Evol.-application

### API

#### Récupérer tous les artistes
> http://localhost:8000/api/artist

##### Récupérer un artiste par son ID
> http://localhost:8000/api/artist/{id}

#### Récupérer un artiste par son nom
> http://localhost:8000/api/artist/?name=Adele

#### Soumettre un artiste avec ses sons
> httpx -m POST http://127.0.0.1:8000/api/artist/ -j '{"name": "Nom", "songs": ["Musique"]}' 

Ne fonctionne pas si l'article existe déjà.

#### Ajouter un son à un artiste

> httpx -m PATCH http://127.0.0.1:8000/api/artist/{ID}/add_song/ -j '{"songs": ["Musique"]}'

Ne fonctionne pas si le son existe déjà.

#### Supprimer un son à un artiste

> httpx -m PATCH http://127.0.0.1:8000/api/artist/{ID}/remove_song/ -j '{"song": "Musique"}'

#### Supprimer un artiste

> httpx -m DELETE http://127.0.0.1:8000/api/artist/{ID}/