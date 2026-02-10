from game.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turno = "X"

    def jugar(self, posicion):
        
        if self.board.resultados() != None:
            return False
        
        resultado = self.board.casilla_marcada(posicion, self.turno) #llama para pasar lo que hay dentro()

        if resultado:
           self.turno = "O" if self.turno == "X" else "X"
           return True
        
        return False
    
    def resultado(self):
        return self.board.resultados()
           
               