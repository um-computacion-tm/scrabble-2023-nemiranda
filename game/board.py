from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.score = {'A': 1, 'B': 3, 'C': 3, 'CH': 5, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
                       'I': 1, 'J': 8, 'L': 1, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3,
                       'Q': 5, 'R': 1, 'RR': 8, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8,
                       'Y': 1, 'Z': 10, 'Comodin': 0}

    @staticmethod
    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value

    def validate_word_inside_board(self, word, location, orientation):
        #WORK IN PROGRESS
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            else:
                return True
        else:
            pass

        def validate_tiles_for_word(self, word, location, orientation, playerTiles):
        N = location[0] - 1 
        M = location[1] - 1
        
        playerTilesToVerify = []
        for i in playerTiles:
            playerTilesToVerify.append(i.letter)
        print (playerTilesToVerify)
        for i in word:
            if i.letter.letter == self.grid[N][M].letter:
                pass
            elif i.letter.letter in playerTilesToVerify:
                playerTilesToVerify.remove(i.letter.letter)
            else:
                return False
                   
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return True

        def validate_connected_words(self,word, location, orientation):
        N = location[0] - 1 
        M = location[1] - 1
        for i in range(len(word)):
            if N == 7 and M == 7 and self.grid[7][7].letter == ' ':
                return True
            if self.grid[N][M].letter != ' ':
                return True
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return False