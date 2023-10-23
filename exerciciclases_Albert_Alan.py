import json
from Character import Character
from Character_films import CharacterFilms

def read_json() -> list: # Llegeix el JSON i retorna una LLISTA de personatges
    json_file = open('StarWars.json')
    data = json.load(json_file)
    characters = []
    for field in data:
        charact = field['fields']
        characters.append(Character(charact['edited'], charact['name'], charact['created'], charact['gender'], charact['skin_color'] , charact['hair_color'] , charact['height'] , charact['eye_color'] , charact['mass'] , charact['homeworld'], charact['birth_year']))
    return characters

characters = read_json()
for character in characters:
    print(character.name, character.gender, character.homeworld, character.birth_year)








