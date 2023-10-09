from game.board import *
from game.players import *
from game.models import *


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.dictionary = []
        for _ in range(players_count):
            self.players.append(Player())

    def give_tiles(self):
        for player in self.players:
            player.add_tiles(self.tilebag.draw_tiles(7))

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        else:            
            index = self.players.index(self.current_player) + 1
            if index >= len(self.players):
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[index]

    def get_words():
        pass

    def put_words():
        pass

    def end_game(self):
        if  self.bag_tiles == []:
            return True
        else:
            return False

class Validate:

    def validate_word(self, word, location, orientation):

        self.board.validate_word_inside_board(word, location, orientation)

        rute = './dictionary.txt' #NEED TO ADD THE DICTIONARY FILE

        word = word.replace(' ', '').lower()
        word = word.replace('á', 'a')
        word = word.replace('é', 'e')
        word = word.replace('í', 'i')
        word = word.replace('ó', 'o')
        word = word.replace('ú', 'u')

        with open(rute, 'r') as archivo_texto:
            contenido = archivo_texto.read().splitlines()

        if word in contenido:
            return True
        else:
            raise NoMatchForWordException("No existe esta palabra")

    def end(self):
        if  self.bag_tiles == []:
            return True
        else:
            return False

if __name__ == '__main__':
    pass
