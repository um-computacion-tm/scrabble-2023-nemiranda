from game.board import Board
from game.players import Player
from game.models import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.dictionary = []
        for _ in range(players_count):
            self.players.append(Player())

    def next_turn(self):
        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0

    def validate_word(self, word, location, orientation):

        self.board.validate_word_inside_board(word, location, orientation)
    
    def get_words():

    def put_words():
