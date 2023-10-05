from game.tile import *

class Cell:
    def __init__(
        self,
        multiplier=1,
        multiplier_type='',
        tile=None,
        multiplier_active=True,
    ):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = multiplier_active
        self.letter = letter

    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
