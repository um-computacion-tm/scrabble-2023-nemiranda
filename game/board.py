from cell import *


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '', ('')) for _ in range(15) ]
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

    def is_empty(self):
        for row in self.grid:
            for cell in row:
                if cell.letter != '':
                    return False
        return True


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

        def superponer(self, word, location, orientation):
            N = location[0] - 1 
            M = location[1] - 1
        for i in word:
            if self.grid[N][M].letter == ' ':
                pass
            elif self.grid[N][M].letter != i:
                return False
            if orientation == 'H':
                M += 1
            elif orientation == 'V':
                N += 1
        return True

        def board_array(self):
            return self.board

        def show_board(self):
            print('')
            columnas = ['   ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
            print("  ".join(columnas))
            print('-------------------------------------------------')
            filas  = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
            for i in range(15):
                print(filas[i], end='|  ')
                for j in range(15):
                    if self.grid[i][j].letter is None:
                        print('-', end='  ')
                    else:
                        print(self.grid[i][j].letter.letter.upper(), end='  ')
                print('')
            print('')
        
        def validate_init(self, word, location, orientation):
                    center_row, center_col = 7, 7
                    if orientation == "H":
                        word_coords = [(location[0], location[1] + i) for i in range(len(word))]
                    elif orientation == "V":
                        word_coords = [(location[0] + i, location[1]) for i in range(len(word))]
                    for coord in word_coords:
                        if coord == (center_row, center_col):
                            return True
                    return False

        def giveTiles(self, positions: list):
            tiles = []
            for i in range(len(positions)):
                tiles.append(self.rack.pop(positions[i]))
                for j in range(len(positions)):
                 if positions[i] < positions[j]:
                        positions[j] -= 1
        return tiles

        def multiplication(self):
                letters = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))
                words = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))

        def cells_board(self, word, location, orientation):
            N = location[0] - 1 
            M = location[1] - 1
            word_cells = []
            word = unidecode(word)
            for i in word:
                word_cells.append(self.grid[N][M])
                if orientation == 'H':
                    M += 1
                elif orientation == 'V':
                    N += 1
            return word_cells

        def replace(self, word):
            word = word.replace('á', 'a')
            word = word.replace('é', 'e')
            word = word.replace('í', 'i')
            word = word.replace('ó', 'o')
            word = word.replace('ú', 'u')
            return word