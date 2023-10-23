import json
from Character import Character

class CharacterFilms(Character):
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year, num_of_films, first_film, alive_at_the_end):
        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self._num_of_films = num_of_films
        self._first_film = first_film
        self._alive_at_the_end = alive_at_the_end
    
        @property
        def num_of_films(self):
            return self._num_of_films
        @property
        def first_film(self):
            return self._first_film
        @property
        def alive_at_the_end(self):
            return self._alive_at_the_end

        @num_of_films.setter
        def num_of_films(self, new_num_of_films):
            self._num_of_films = new_num_of_films
        @first_film.setter
        def first_film(self, new_first_film):
            self._first_film = new_first_film
        @alive_at_the_end.setter
        def alive_at_the_end(self, new_alive_at_the_end):
            self._alive_at_the_end = new_alive_at_the_end

    # EXERCICI 2
    def print_Info(self):
        if self._num_of_films != "Null":
            print("EXTRA: ", self.name, self._num_of_films, self._first_film, self._alive_at_the_end)
    
   