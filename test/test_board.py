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

    def test_calculate_word_value():
        # Test case 1: No multipliers
        word1 = [Cell('A', 1, None, None, True), Cell('B', 3, None, None, True), Cell('C', 1, None, None, True)]
        assert calculate_word_value(word1) == 5

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

    def test_word_connected(self):
        board1 = Board()
        board1.grid[7][7].letter.letter = 'V'
        board1.grid[7][8].letter.letter = 'A'
        board1.grid[7][9].letter.letter = 'S'
        board1.grid[7][10].letter.letter = '0'
        location = [7,9]
        orientation = 'V'
        word = 'CASA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertTrue(result)

    def test_word_not_connected(self):
        board1 = Board()
        board1.grid[7][7].letter = 'V'
        board1.grid[7][8].letter = 'A'
        board1.grid[7][9].letter = 'S'
        board1.grid[7][10].letter = '0'
        location = [2,2]
        orientation = 'V'
        word = 'CASA'
        result = board1.validate_word_is_connected(word, location, orientation)
        self.assertFalse(result)

    def test_superponer(self):
        self.grid = [[' ' for _ in range(5)] for _ in range(5)]  # Ejemplo de cuadrícula vacía
        self.grid[1][1] = 'A'  # Establecer una letra 'A' en la posición (1, 1)

    def test_board_array(self):
        # Create an instance of the ScrabbleBoard class
        scrabble_board = ScrabbleBoard()

        # Get the board array using the board_array method
        board = scrabble_board.board_array()

        # Check if the board is a list of lists and has the expected dimensions
        self.assertIsInstance(board, list)
        self.assertEqual(len(board), 15)
        self.assertTrue(all(isinstance(row, list) and len(row) == 15 for row in board))

    def test_show_board(self):
        # Create an instance of the ScrabbleBoard class
        scrabble_board = ScrabbleBoard()

        # Call the show_board method
        scrabble_board.show_board()

        # Capture the printed content
        printed_content = self.captured_output.getvalue()

        # Define your expected board representation (modify this as needed)
        expected_board = """
           A   B   C   D   E   F   G   H   I   J   K   L   M   N   O
    -------------------------------------------------
    01|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    02|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    03|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    04|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    05|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    06|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    07|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    08|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    09|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    10|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    11|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    12|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    13|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    14|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
    15|  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  
        """

        # Remove leading/trailing whitespace for comparison
        printed_content = printed_content.strip()
        expected_board = expected_board.strip()

        # Assert that the printed content matches the expected board
        self.assertEqual(printed_content, expected_board)

    def test_validate_init(self):
        # Create an instance of the ScrabbleBoard class
        scrabble_board = ScrabbleBoard()

        # Test with a horizontal word at the center
        word1 = "WORD"
        location1 = (7, 5)
        orientation1 = "H"
        self.assertTrue(scrabble_board.validate_init(word1, location1, orientation1))

        # Test with a vertical word at the center
        word2 = "TEST"
        location2 = (5, 7)
        orientation2 = "V"
        self.assertTrue(scrabble_board.validate_init(word2, location2, orientation2))

        # Test with a word that doesn't start at the center
        word3 = "PYTHON"
        location3 = (1, 1)
        orientation3 = "H"
        self.assertFalse(scrabble_board.validate_init(word3, location3, orientation3))

    def testGiveTiles(self):
        player = Player()
        tile1 = Tile('N', 1)
        tile2 = Tile('I', 1)
        tile3 = Tile('M', 3)
        tile4 = Tile('A', 1)
        tile5 = Tile('O', 1)
        tile6 = Tile('A', 1)
        tile7 = Tile('D', 2)
        tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7]
        player.takeTiles(tiles) 
        result = player.giveTiles([0, 3, 6, 4])
        self.assertEqual(result, [tile1, tile4, tile7, tile5]) 
        self.assertEqual(player.rack, [tile2, tile3, tile6])

    def test_multiplication(self):
        # Create an instance of the ScrabbleBoard class
        scrabble_board = ScrabbleBoard()

        # Define the expected letters and words tuples
        expected_letters = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))
        expected_words = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))

        # Call the multiplication method
        result = scrabble_board.multiplication()

        # Check if the result matches the expected tuples
        self.assertEqual(result[0], expected_letters)
        self.assertEqual(result[1], expected_words)

    def test_cells_board(self):
        board1 = Board()
        board1.grid[7][7].letter = Tile('C', 1)
        board1.grid[7][8].letter = Tile('A', 1)
        board1.grid[7][9].letter = Tile('S', 1)
        board1.grid[7][10].letter = Tile('A', 1)
        cells = board1.cells_board('TASA', [8,8], 'H')
        self.assertEqual(cells, [board1.grid[7][7],board1.grid[7][8],board1.grid[7][9],board1.grid[7][10]])

    def test_replace(self):
        board=Board()
        word = 'fácil'
        self.assertEqual(board.remove_accent(word),'facil')

class TestSquare(unittest.TestCase):
    def test_initialization(self):
        square = Square()
        self.assertEqual(square.row, 0)
        self.assertEqual(square.column, 0)
        self.assertIsNone(square.multiplier_type)
        self.assertIsNone(square.tile)

    def test_add_tile(self):
        square = Square()
        tile = Tile('A', 1)  # Assuming you have a Tile class defined somewhere
        square.add_tile(tile)
        self.assertEqual(square.tile, tile)

    def test_calculate_score_letter_no_tile(self):
        square = Square()
        score = square.calculate_score_letter()
        self.assertEqual(score, 0)

    def test_calculate_score_letter_without_multiplier(self):
        square = Square()
        tile = Tile('A', 1)  # Assuming you have a Tile class defined somewhere
        square.add_tile(tile)
        score = square.calculate_score_letter()
        self.assertEqual(score, 1)

    def test_calculate_score_letter_DL_multiplier(self):
        square = Square(multiplier_type='DL')
        tile = Tile('A', 1)  # Assuming you have a Tile class defined somewhere
        square.add_tile(tile)
        score = square.calculate_score_letter()
        self.assertEqual(score, 2)

    def test_calculate_score_letter_TL_multiplier(self):
        square = Square(multiplier_type='TL')
        tile = Tile('A', 1)  # Assuming you have a Tile class defined somewhere
        square.add_tile(tile)
        score = square.calculate_score_letter()
        self.assertEqual(score, 3)

if __name__ == '__main__':
    unittest.main()