class Board:
    def __init__(self):
        self.casillas = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    
    def casilla_marcada(self, posicion, ficha):

        if (ficha not in ["X", "O"]) or (posicion < 0 or posicion > 8):
            return False
        
        if self.casillas[posicion] != "-":
            return False
        
        self.casillas[posicion] = ficha
        return True

    def resultados(self):
        jugadas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticales
        [0, 4, 8], [2, 4, 6]             # Diagonales
        ]

        for combo in jugadas:
            a, b, c = combo

            if self.casillas[a] == self.casillas[b] == self.casillas[c] and self.casillas[a] != "-":
                return self.casillas[a]
            
        return None