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
        if self.current_player == None:
            self.current_player = self.players[0]
        else:            
            index = self.players.index(self.current_player) + 1
            if index >= len(self.players):
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[index]


    def validate_word(self, word, location, orientation):

        self.board.validate_word_inside_board(word, location, orientation)
    
    def get_words():
        pass

    def put_words():
        pass

if __name__ == '__main__':
    pass
