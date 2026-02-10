import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game.game import Game
from game.board import Board
import unittest

class TestGame(unittest.TestCase):

    def test_inicio(self):
        game = Game()
        self.assertTrue(isinstance(game.board, Board)) #isinstance comprueba si un objeto es una instancia de una clase específica o de una subclase de esta
    
    def test_primera_jugada(self):
        game = Game()
        self.assertEqual (game.turno, "X")
    
    def test_cambio_turno(self):
        game = Game()
        game.jugar(0)
        self.assertEqual (game.turno, "O")
    
    def test_cambio_turno_falla(self):
        game = Game()
        game.jugar(0)
        game.jugar(0)
        self.assertEqual (game.turno, "O")
    
    def test_no_jugar_despues_de_ganar(self):
        game = Game()

        game.jugar(0)
        game.jugar(3)
        game.jugar(1)
        game.jugar(4)
        game.jugar(2)

        jugada_extra = game.jugar(5)
        
        self.assertFalse(jugada_extra)

if __name__ == "__main__":
    unittest.main()
