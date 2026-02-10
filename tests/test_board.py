import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game.board import Board
import unittest

class TestBoard(unittest.TestCase):
    def test_board_casillas(self):
        board = Board()
        self.assertEqual(len(board.casillas), 9)
    
    def test_board_casillas_iniciales_vacias(self):
        board = Board()
        self.assertEqual(all(casilla == "-" for casilla in board.casillas), True)
    
    def test_barrido(self):
        tablero = Board()
        tablero.casilla_marcada(0, "X")
        original_casilla = tablero.casillas[0]
        tablero.casilla_marcada(0, "X")
        self.assertEqual(tablero.casillas[0], original_casilla)
    
    def test_board_verificar_cas_llena(self):
        tablero_vacio = Board()
        tablero_vacio.casilla_marcada(0, "X")
        board_lugar_ocupado = ["X", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.assertEqual(tablero_vacio.casillas, board_lugar_ocupado)
    
    def test_board_rechaza_datos_invalidos(self):
        tablero = Board()
        tablero.casilla_marcada(0, "U")
        tablero.casilla_marcada(99, "X")
        self.assertEqual(all(casilla == "-" for casilla in tablero.casillas), True)
    
    def test_sin_ganador(self):
        tablero = Board()
        tablero.casilla_marcada(0, "X")
        tablero.casilla_marcada(5, "O")
        self.assertIsNone(tablero.resultados())

    def test_jugada(self):
        jugada = Board()
        jugada.casillas = ["X", "O", "X",
                           "O", "X", "O",
                           "O", "O", "X"]
        self.assertIn(jugada.resultados(), ["X", "O"])
    
    def test_empate(self):
        jugada = Board()
        jugada.casillas = ["O", "X", "X",
                           "X", "X", "O",
                           "O", "O", "X"]
        self.assertIsNone(jugada.resultados(), None) #¿esto es la nada misma?

if __name__ == "__main__":
    unittest.main()
