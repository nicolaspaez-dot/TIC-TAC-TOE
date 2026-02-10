from game.ai import MinimaxAI
import random

class Player:
    def __init__(self, ficha): #variables temporales
        self.ficha = ficha

class HumanPlayer(Player):
    def __init__(self, ficha, nombre="Humano"):
        super().__init__(ficha)
        self.nombre = nombre

class AIPlayer:
    def __init__(self, ficha, dificultad="dificil"):
        self.ficha = ficha
        self.nombre = "Ricochet"
        self.dificultad = dificultad
        # Crea el motor de IA
        self.motor_ia = MinimaxAI(ficha)

    def seleccionar_movimiento(self, tablero):
        if self.dificultad == "normal":
           
            disponibles = [i for i, x in enumerate(tablero.casillas) if x == "-"]
            if disponibles:
                return random.choice(disponibles)
            return None
        elif self.dificultad == "medio":
           
            disponibles = [i for i, x in enumerate(tablero.casillas) if x == "-"] #enumerate devuelve indice y contenido 
            
            if random.random() < 0.5 and disponibles: #50% chance
                 return random.choice(disponibles)
            else:
                 return self.motor_ia.calcular_mejor_movimiento(tablero)
        else:
            # Usamos el motor
            return self.motor_ia.calcular_mejor_movimiento(tablero)
    

