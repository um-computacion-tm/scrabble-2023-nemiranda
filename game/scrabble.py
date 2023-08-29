from game.board import Board
from game.player import Player
from game.models import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.player = []
        self.dictionary = []
        for _ in range(players_count):
            self.players.append(Player())
