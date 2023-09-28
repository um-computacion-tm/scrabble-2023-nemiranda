import unittest
from game.board import *
from game.cell import *
from game.models import *
from game.tile import *


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter='C', points=1, ''),
            Cell(letter='A', points=1, ''),
            Cell(letter='S', points=2),
            Cell(letter='A', points=1, ''),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter='C', points=1, ''),
            Cell(letter='A', points=1, ''),
            Cell(
                letter=Tile('S', 1, '',
                multiplier=2,
                multiplier_type='letter',
            )),
            Cell(letter=Tile('A', points=1, '')),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1, '')),
            Cell(letter=Tile('A', 1, '')),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, '')),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1, '')
            ),
            Cell(letter=Tile('A', 1, '')),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, '')),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        # QUE HACEMOS CON EL ACTIVE ????
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1, '')
            ),
            Cell(letter=Tile('A', 1, '')),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1, '')),
        ]
        value = calculate_word_value(word)
        self.assertEqual(value, 5)

class ValidateSpecialCases(unittest.TestCase)



if __name__ == '__main__':
    unittest.main()