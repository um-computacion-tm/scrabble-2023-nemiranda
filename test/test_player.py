import unittest
from game.players import *
from game.models import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_add_tiles_to_empty_collection(self):
        game = YourGameObject([])
        game.add_tiles(['A', 'B', 'C'])
        self.assertEqual(game.tiles, ['A', 'B', 'C'])

    def test_add_tiles_to_non_empty_collection(self):
        game = YourGameObject(['D', 'E'])
        game.add_tiles(['A', 'B', 'C'])
        self.assertEqual(game.tiles, ['D', 'E', 'A', 'B', 'C'])

    def test_change_tiles_single_tile(self):
        game = YourGameObject(['A', 'B', 'C', 'D', 'E'])
        old_indices = [2]
        new_tiles = ['X']
        changed = game.change_tiles(old_indices, new_tiles)
        self.assertEqual(changed, ['B'])
        self.assertEqual(game.tiles, ['A', 'X', 'C', 'D', 'E'])

    def test_change_tiles_multiple_tiles(self):
        game = YourGameObject(['A', 'B', 'C', 'D', 'E'])
        old_indices = [1, 3, 5]
        new_tiles = ['X', 'Y', 'Z']
        changed = game.change_tiles(old_indices, new_tiles)
        self.assertEqual(changed, ['A', 'C', 'E'])
        self.assertEqual(game.tiles, ['X', 'B', 'Y', 'D', 'Z'])

    def test_show_tiles_empty_collection(self):
        game = YourGameObject([])
        result = game.show_tiles()
        self.assertEqual(result, [])

    def test_show_tiles_non_empty_collection(self):
        tiles = [Tile('A'), Tile('B'), Tile('C')]
        game = YourGameObject(tiles)
        result = game.show_tiles()
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, False)

    def testaddscore(self):
        player = Player()
        self.assertEqual(player.score, 0)
        player.addscore(15)
        self.assertEqual(player.score, 9)
        player.addscore(32)
        self.assertEqual(player.score, 20)

    def test_mix_tiles(self):
        game = ScrabbleGame(1)
        player_1 = game.players[0]
        original_tiles = player_1.tiles.copy()
        player_1.mix_tiles()
        self.assertNotEqual(original_tiles, player_1.tiles)

if __name__ == '__main__':
    unittest.main()