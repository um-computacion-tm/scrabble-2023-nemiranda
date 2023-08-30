import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), #x12
            Tile('E', 1), #x12
            Tile('I', 1), #x6
            Tile('L', 1), #x4
            Tile('N', 1), #x5
            Tile('O', 1), #x9
            Tile('R', 1), #x5
            Tile('S', 1), #x6
            Tile('T', 1), #x4
            Tile('U', 1), #x5
            Tile('D', 2), #x5
            Tile('G', 2), #x2
            Tile('B', 3), #x2
            Tile('C', 3), #x4
            Tile('M', 3), #x2
            Tile('P', 3), #x2
            Tile('F', 4), #x1
            Tile('H', 4), #x2
            Tile('V', 4), #x1
            Tile('Y', 4), #x1
            Tile('CH', 5), #x1
            Tile('Q', 5), #x1
            Tile('J', 8), #x1
            Tile('LL', 8), #x1
            Tile('Ñ', 8), #x1
            Tile('RR', 8), #x1
            Tile('X', 8), #x1
            Tile('Z', 10), #x1
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
