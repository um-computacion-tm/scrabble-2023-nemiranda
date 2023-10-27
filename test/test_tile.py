import unittest
from game.tile import *

class TestTile(unittest.TestCase):
    def test_tile_initialization(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestComodin(unittest.TestCase):
    def setUp(self):
        # Create a list of available tiles for testing
        self.available_tiles = [{'letter': 'A', 'value': 1}, {'letter': 'B', 'value': 3}]
        self.comodin = Comodin('C', 0)

    def test_comodin_initialization(self):
        self.assertEqual(self.comodin.letter, 'C')
        self.assertEqual(self.comodin.value, 0)

    def test_elector_valid_letter(self):
        self.comodin.elector('A')
        self.assertEqual(self.comodin.letter, 'A')
        self.assertEqual(self.comodin.value, 0)

    def test_elector_invalid_letter(self):
        with self.assertRaises(EmptyTiles):
            self.comodin.elector('D')

    def test_remaingtiles(self):
        self.comodin.tiles = self.available_tiles  # Assuming you have a 'tiles' attribute
        remaining = self.comodin.remaingtiles()
        self.assertEqual(remaining, len(self.available_tiles))

if __name__ == '__main__':
    unittest.main()