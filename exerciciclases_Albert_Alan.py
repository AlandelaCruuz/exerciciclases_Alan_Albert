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

def load_character_films(characters):
    characters_films = []

    for character in characters:
        if character.name == "Luke Skywalker":
            data = ["4", "Star Wars: Episode IV - A New Hope (1977)", "dead"]
        elif character.name == "Chewbacca":
            data = ["6", "Star Wars: Episode IV - A New Hope (1977)", "alive"]
        elif character.name == "Anakin Skywalker":
            data = ["4", "Star Wars: Episode VI - Return of the Jedi (1983)", "dead"]
        else:
            data = ["Null", "Null", "Null"]

        character_films = CharacterFilms(
            name=character._name,
            created=character._created,
            skin_color=character._skin_color,
            edited=character._edited,
            gender=character._gender,
            hair_color=character._hair_color,
            height=character._height,
            eye_color=character._eye_color,
            mass=character._mass,
            homeworld=character._homeworld,
            birth_year=character._birth_year,
            num_of_films=data[0],
            first_film=data[1],
            alive_at_the_end=data[2]
        )
        characters_films.append(character_films)

    return characters_films 

# Importa las clases y funciones necesarias

characters_films = load_character_films(read_json())


# Imprimir información de los personajes con películas
for character in characters_films:
    character.print_Info()


# Exportar dades de tots els personatges en un nou document JSON
def export_json(characters_films):
    json_file = open('newStarWars.json', 'w')
    data = []
    for character in characters_films:
        data.append({
            "edited": character._edited,
            "name": character._name,
            "created": character._created,
            "gender": character._gender,
            "skin_color": character._skin_color,
            "hair_color": character._hair_color,
            "height": character._height,
            "eye_color": character._eye_color,
            "mass": character._mass,
            "homeworld": character._homeworld,
            "birth_year": character._birth_year,
            "num_of_films": character._num_of_films,
            "first_film": character._first_film,
            "alive_at_the_end": character._alive_at_the_end
        })
    json.dump(data, json_file, indent=4)
    json_file.close()

export_json(characters_films)






