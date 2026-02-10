import math

class MinimaxAI:
    def __init__(self, ficha_ia, profundidad=None):
        self.ficha_ia = ficha_ia
        self.ficha_rival = "X" if ficha_ia == "O" else "O"
        self.profundidad_max = profundidad

    def calcular_mejor_movimiento(self, tablero):
        mejor_puntaje = -math.inf
      
        disponibles = [i for i, x in enumerate(tablero.casillas) if x == "-"]
        
      
        if not disponibles:
            return None
            
       
        movimiento = disponibles[0] 
        
        for i in disponibles:
            tablero.casillas[i] = self.ficha_ia
            puntaje = self._minimax(tablero, 0, False, -math.inf, math.inf)
            tablero.casillas[i] = "-"
            
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                movimiento = i
                
        return movimiento
    def _minimax(self, tablero, profundidad, es_maximizando, alpha, beta):
        
        ganador = tablero.resultados()
        if ganador == self.ficha_ia: return 10 - profundidad
        if ganador == self.ficha_rival: return profundidad - 10
        if "-" not in tablero.casillas: return 0
        
        # Límite de profundidad (si se configuró)
        if self.profundidad_max is not None and profundidad >= self.profundidad_max:
            return 0

        if es_maximizando:
            mejor_puntaje = -math.inf
            for i in range(9):
                if tablero.casillas[i] == "-":
                    tablero.casillas[i] = self.ficha_ia
                    puntaje = self._minimax(tablero, profundidad + 1, False, alpha, beta)
                    tablero.casillas[i] = "-"
                    mejor_puntaje = max(puntaje, mejor_puntaje)
                    alpha = max(alpha, mejor_puntaje)
                    if beta <= alpha: break
            return mejor_puntaje
        else:
            mejor_puntaje = math.inf
            for i in range(9):
                if tablero.casillas[i] == "-":
                    tablero.casillas[i] = self.ficha_rival
                    puntaje = self._minimax(tablero, profundidad + 1, True, alpha, beta)
                    tablero.casillas[i] = "-"
                    mejor_puntaje = min(puntaje, mejor_puntaje)
                    beta = min(beta, mejor_puntaje)
                    if beta <= alpha: break
            return mejor_puntaje