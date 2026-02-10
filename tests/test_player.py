import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game.player import HumanPlayer, AIPlayer
from game.board import Board
import unittest

class TestPlayer(unittest.TestCase):

    def test_creacion(self):
        player = HumanPlayer("X", "Nico")

        self.assertEqual(player.nombre, "Nico")

      
        self.assertEqual(player.ficha, "X")
    
    def test_nombre_ia(self):
        surge = AIPlayer("X")
        self.assertEqual(surge.nombre, "Ricochet")

class TestAI(unittest.TestCase):
    def test_ia_gana_en_una_jugada(self):

        tablero = Board()
        tablero.casillas = [
            "O", "O", "-", 
            "X", "X", "-", 
            "-", "-", "-"
        ]
        bot = AIPlayer("O", dificultad="dificil")
        
        movimiento = bot.seleccionar_movimiento(tablero)
        self.assertEqual(movimiento, 2)

    def test_ia_bloquea_al_humano(self):

        tablero = Board()
        tablero.casillas = [
            "X", "X", "-", 
            "O", "-", "-", 
            "-", "-", "-"
        ]
        bot = AIPlayer("O", dificultad="dificil")
        
        movimiento = bot.seleccionar_movimiento(tablero)
        self.assertEqual(movimiento, 2)

    def test_ia_normal_mueve_random(self):
        tablero = Board()
        # Llenamos algunas casillas
        tablero.casillas = ["X", "-", "O", "-", "X", "-", "-", "-", "-"]
        bot = AIPlayer("O", dificultad="normal")
        movimiento = bot.seleccionar_movimiento(tablero)
        
        # Debe ser una de las vacías: 1, 3, 5, 6, 7, 8
        self.assertIn(movimiento, [1, 3, 5, 6, 7, 8])
        self.assertTrue(tablero.casillas[movimiento] == "-")

if __name__ == "__main__":
    unittest.main()