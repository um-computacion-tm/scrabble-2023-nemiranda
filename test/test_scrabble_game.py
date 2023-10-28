import unittest
from board import *
from players import *
from models import *
from game.scrabble import *

class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        # Initialize a ScrabbleGame with 2 players for testing
        self.game = ScrabbleGame(players_count=2)

    def test_give_tiles(self):
        # Ensure that tiles are given to players
        self.game.give_tiles()
        for player in self.game.players:
            self.assertEqual(len(player.tiles), 7)

    def test_next_turn(self):
        # Test the next_turn function
        self.game.next_turn()
        self.assertEqual(self.game.current_player, self.game.players[1])

    def test_end_game(self):
        # Test the end_game function with an empty bag_tiles
        self.game.bag_tiles.tiles = []
        self.assertTrue(self.game.end_game())

class TestValidate(unittest.TestCase):
    def setUp(self):
        # Initialize a Validate object
        self.validator = Validate()

    def test_validate_word(self):
        # Test word validation with a valid word
        self.assertTrue(self.validator.validate_word("test", (0, 0), "H"))

    def test_validate_word_invalid(self):
        # Test word validation with an invalid word
        with self.assertRaises(NoMatchForWordException):
            self.validator.validate_word("xyz", (0, 0), "H")

    def test_end(self):
        # Test the end function with an empty bag_tiles
        self.validator.bag_tiles.tiles = []
        self.assertTrue(self.validator.end())

if __name__ == '__main__':
    unittest.main()