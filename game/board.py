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


