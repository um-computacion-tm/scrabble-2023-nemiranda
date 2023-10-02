import unittest
from game.board import *
from game.tile import *


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)  
    
        assert word_is_valid == True
    
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty == False

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_word_valide_acento_and_spaces(self):
            val = Validate()
            word = 'ár bol'
            self.assertTrue(
                val.validate_word(word)
            )
    
    def test_not_empty(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (6,7)
        orientation = 'V'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)


    def test_superponer(self):
        self.grid = [[' ' for _ in range(5)] for _ in range(5)]  # Ejemplo de cuadrícula vacía
        self.grid[1][1] = 'A'  # Establecer una letra 'A' en la posición (1, 1)

    def test_superponer_horizontal_exitoso(self):
        # Prueba de superposición horizontal exitosa
        obj = ClaseGrid(self.grid)  # Supongamos que ClaseGrid toma la cuadrícula como argumento
        self.assertTrue(obj.supeponer("ABC", (1, 1), "H"))

    def test_superponer_horizontal_fallido(self):
        # Prueba de superposición horizontal fallida
        obj = ClaseGrid(self.grid)
        self.assertFalse(obj.supeponer("ADC", (1, 1), "H"))

    def test_superponer_vertical_exitoso(self):
        # Prueba de superposición vertical exitosa
        obj = ClaseGrid(self.grid)
        self.assertTrue(obj.supeponer("ABC", (1, 1), "V"))

    def test_superponer_vertical_fallido(self):
        # Prueba de superposición vertical fallida
        obj = ClaseGrid(self.grid)
        self.assertFalse(obj.supeponer("ADC", (1, 1), "V"))

if __name__ == '__main__':
    unittest.main()