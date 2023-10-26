import unittest
from game.models import *
from game.tile import *
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_draw_tiles_valid_quantity(self):
        game = YourGameObject(['A', 'B', 'C', 'D', 'E'])
        drawn_tiles = game.draw_tiles(3)
        self.assertEqual(drawn_tiles, ['E', 'D', 'C'])
        self.assertEqual(game.tiles, ['A', 'B'])

    def test_draw_tiles_too_many_tiles_requested(self):
        game = YourGameObject(['A', 'B'])
        drawn_tiles = game.draw_tiles(3)
        self.assertEqual(drawn_tiles, [])
        self.assertEqual(game.tiles, ['A', 'B'])

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            102,
        )

    def test_tiles_remaining_empty_tiles(self):
        game = YourGameObject([])
        remaining = game.tiles_remaining()
        self.assertEqual(remaining, 0)

    def test_tiles_remaining_non_empty_tiles(self):
        game = YourGameObject(['A', 'B', 'C', 'D', 'E'])
        remaining = game.tiles_remaining()
        self.assertEqual(remaining, 5)

    def test_left_tiles_empty_bag(self):
        # Test when the bag is empty
        self.game.bag = []
        self.assertEqual(self.game.left_tiles(), 0)

    def test_left_tiles_non_empty_bag(self):
        # Test when the bag has some tiles
        self.game.bag = ['A', 'B', 'C', 'D']
        self.assertEqual(self.game.left_tiles(), 4)
    
    class TestInitialization(unittest.TestCase):
        def test_initialization(self):
            scrabble_tiles = ScrabbleTiles()
            tiles_count = scrabble_tiles.tiles_left()
            assert tiles_count == 100

    def test_exceptiontake(self):
        bag = BagTiles()
        tiles_taken = bag.take(97)
        with self.assertRaises(NoTilesInTheBagException):
            tiles = bag.take(1)
        self.assertEqual(
            bag.lef_tiles(),
            (0)
        )

if __name__ == '__main__':
    unittest.main()
