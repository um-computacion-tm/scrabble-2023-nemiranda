TILES=[
    {"l": "_", "v": 0, "n": 2},
    {"l": "A", "v": 1, "n": 12},
    {"l": "B", "v": 3, "n": 2},
    {"l": "C", "v": 3, "n": 4},
    {"l": "CH", "v": 5, "n": 1},
    {"l": "D", "v": 2, "n": 5},
    {"l": "E", "v": 1, "n": 12},
    {"l": "F", "v": 4, "n": 1},
    {"l": "G", "v": 2, "n": 2},
    {"l": "H", "v": 4, "n": 2},
    {"l": "I", "v": 1, "n": 6},
    {"l": "J", "v": 8, "n": 1},
    {"l": "L", "v": 1, "n": 4},
    {"l": "LL", "v": 8, "n": 1},
    {"l": "M", "v": 3, "n": 2},
    {"l": "N", "v": 1, "n": 5},
    {"l": "Ñ", "v": 8, "n": 1},
    {"l": "O", "v": 1, "n": 9},
    {"l": "P", "v": 3, "n": 2},
    {"l": "Q", "v": 5, "n": 1},
    {"l": "R", "v": 1, "n": 5},
    {"l": "RR", "v": 8, "n": 1},
    {"l": "S", "v": 1, "n": 6},
    {"l": "T", "v": 1, "n": 4},
    {"l": "U", "v": 1, "n": 5},
    {"l": "V", "v": 4, "n": 1},
    {"l": "X", "v": 8, "n": 1},
    {"l": "Y", "v": 4, "n": 1},
    {"l": "Z", "v": 10, "n": 1},
]

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class Comodin:
    def __init__(self, letter, value):
        super().__init__(letter, value)


    def elector(self,letter_comodin):
        for i in TILES:
            if i['letter']==letter_comodin.upper():
                self.letter=letter_comodin.upper()
                self.value=0
                break
        else:
            raise EmptyTiles