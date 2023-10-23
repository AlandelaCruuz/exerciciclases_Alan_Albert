class Character:
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        self._edited = edited
        self._name = name
        self._created = created
        self._gender = gender
        self._skin_color = skin_color
        self._hair_color = hair_color
        self._height = height
        self._eye_color = eye_color
        self._mass = mass
        self._homeworld = homeworld
        self._birth_year = birth_year
    @property
    def name(self):
        return self._name
    @property
    def gender(self):
        return self._gender
    @property
    def homeworld(self):
        return self._homeworld
    @property
    def birth_year(self):
        return self._birth_year