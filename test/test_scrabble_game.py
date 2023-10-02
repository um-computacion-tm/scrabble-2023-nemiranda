import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_end(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertFalse(scrabble_game.end())
        scrabble_game.bag_tiles=[]
        self.assertTrue(scrabble_game.end())

if __name__ == '__main__':
    unittest.main()