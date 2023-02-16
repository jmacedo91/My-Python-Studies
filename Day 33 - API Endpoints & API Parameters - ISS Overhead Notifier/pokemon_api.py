import requests
import urllib.request


for _ in range(1, 152):
    response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{_}/")

    data = response.json()
    pokemon = data["name"]
    url_sprite = data["forms"][0]["url"]
    poke_photo = requests.get(url=url_sprite)
    pokemon_form = poke_photo.json()
    url_front = pokemon_form["sprites"]["front_default"]
    urllib.request.urlretrieve(url=url_front, filename=f"pokemon_sprites/{_}_{pokemon}.png")

