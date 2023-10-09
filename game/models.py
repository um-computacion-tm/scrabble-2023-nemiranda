import random
from game.tile import *

class TileBag:
    def __init__(self):
        self.tiles=[]
        for i in DATA:
            for j in range(i.get('quantity')):
                self.tiles.append(Tile(i.get("letter"),i.get("value")))
        random.shuffle(self.tiles)
 
    def draw_tiles(self,quantity):
        tile_drawn=[]
        try:
            if quantity>len(self.tiles):
                raise TooMuchTiles
            else:
                for i in range(quantity):
                    tile_drawn.append(self.tiles.pop())
                return tile_drawn
        except TooMuchTiles:
            return tile_drawn

    def put_tiles(self,tiles:list):
        try:
            if len(tiles)+len(self.tiles)<=TOTALTILES:
                self.tiles.extend(tiles)
            else:
                raise TooMuchTilesPut
        except TooMuchTilesPut:
            return TooMuchTilesPut

    def tiles_remaining(self):
        return len(self.tiles)

class BagTiles:

    def __init__(self):
        self.tiles = [
            Tile('CH', 5),  #1 ficha CH valor 5
            Tile('F', 4),   #1 ficha F valor 4
            Tile('J', 8),   #1 ficha J valor 8
            Tile('LL', 8),  #1 ficha LL valor 8
            Tile('Ñ', 8),   #1 ficha Ñ valor 8
            Tile('Q', 5),   #1 ficha Q valor 5
            Tile('RR', 8),  #1 ficha RR valor 8
            Tile('V', 4),   #1 ficha V valor 4
            Tile('X', 8),   #1 ficha X valor 8
            Tile('Y', 4),   #1 ficha Y valor 4
            Tile('Z', 10),  #1 ficha Z valor 10
        ]

        for i in range (0,2,1): #2 fichas P valor 3
            self.tiles.append(Tile('P', 3))
        for i in range (0,2,1): #2 fichas B valor 3
            self.tiles.append(Tile('B', 3))
        for i in range (0,2,1): #2 fichas G valor 2
            self.tiles.append(Tile('G', 2))
        for i in range (0,2,1): #2 fichas M valor 3
            self.tiles.append(Tile('M', 3))
        for i in range (0,2,1): #2 fichas H valor 4
            self.tiles.append(Tile('H', 4))
        for i in range (0,2,1): #2 COMODINES
            self.tiles.append(Tile('A', 0))
        for i in range (0,6,1): #6 fichas S valor 1
            self.tiles.append(Tile('S', 1))
        for i in range (0,4,1): #4 fichas C valor 3
            self.tiles.append(Tile('C', 3))
        for i in range (0,9,1): #9 fichas O valor 1
            self.tiles.append(Tile('O', 1))
        for i in range (0,4,1): #4 fichas T valor 1
            self.tiles.append(Tile('T', 1))
        for i in range (0,4,1): #4 fichas L valor 1
            self.tiles.append(Tile('L', 1))
        for i in range (0,5,1): #5 fichas U valor 1
            self.tiles.append(Tile('U', 1))
        for i in range (0,12,1): #12 fichas E valor 1
            self.tiles.append(Tile('E', 1))
        for i in range (0,12,1): #12 fichas A valor 1
            self.tiles.append(Tile('A', 1))
        for i in range (0,5,1): #5 fichas R valor 1
            self.tiles.append(Tile('R', 1))
        for i in range (0,6,1): #6 fichas I valor 1
            self.tiles.append(Tile('I', 1))
        for i in range (0,5,1): #5 fichas N valor 1
            self.tiles.append(Tile('N', 1))
        for i in range (0,5,1): #5 fichas D valor 2
            self.tiles.append(Tile('D', 2))
            
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
