import os
import time
from colorama import Fore, Style
from game.board import Board
from ui.console_ui import ConsoleUI

class GameController:
    """Controla el flujo del juego: turnos, detección de victoria, renderizado."""
    
    def __init__(self, history_manager):
        self.history_manager = history_manager
        self.ui = ConsoleUI()
    
    def jugar_partida(self, nombre_x, nombre_o, bot_x, bot_o):
        """Ejecuta una partida completa.
        
        Args:
            nombre_x: Nombre del jugador X
            nombre_o: Nombre del jugador O
            bot_x: Bot para X (None si es humano)
            bot_o: Bot para O (None si es humano)
        """
        nombres = {"X": nombre_x, "O": nombre_o}
        tablero = Board()
        ficha_actual = "X"
        
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            self.ui.mostrar_tablero(tablero.casillas)
            
            # Obtener movimiento
            pos = self._obtener_movimiento(ficha_actual, nombre_x, nombre_o, bot_x, bot_o, tablero)
            
            # Procesar movimiento
            if pos is not None and tablero.casilla_marcada(pos, ficha_actual):
                # Verificar si hay ganador
                ganador = tablero.resultados()
                
                if ganador:
                    self._mostrar_victoria(tablero, ganador, nombres)
                    break
                
                # Verificar empate
                if "-" not in tablero.casillas:
                    self._mostrar_empate(tablero)
                    break
                
                # Cambiar turno
                ficha_actual = "O" if ficha_actual == "X" else "X"
            else:
                if pos is not None:
                    print(f"{Fore.RED}Movimiento inválido.{Style.RESET_ALL}")
                    time.sleep(1)
        
        input("\nPresioná Enter para volver al menú...")
    
    def _obtener_movimiento(self, ficha_actual, nombre_x, nombre_o, bot_x, bot_o, tablero):
        """Obtiene el movimiento del jugador actual."""
        if ficha_actual == "X":
            if bot_x:
                print(f"\n{nombre_x} pensando...")
                time.sleep(1)
                return bot_x.seleccionar_movimiento(tablero)
            else:
                return self.ui.pedir_jugada(nombre_x)
        else:
            if bot_o:
                print(f"\n{nombre_o} pensando...")
                time.sleep(1)
                return bot_o.seleccionar_movimiento(tablero)
            else:
                return self.ui.pedir_jugada(nombre_o)
    
    def _mostrar_victoria(self, tablero, ganador, nombres):
        """Muestra la pantalla de victoria."""
        os.system("clear" if os.name == "posix" else "cls")
        self.ui.mostrar_tablero(tablero.casillas)
        msg = f"Ganador: {nombres[ganador]} ({ganador})"
        print(f"\n{Fore.YELLOW}¡FINAL DE LA PARTIDA! {msg}{Style.RESET_ALL}")
        self.history_manager.guardar(msg)
    
    def _mostrar_empate(self, tablero):
        """Muestra la pantalla de empate."""
        os.system("clear" if os.name == "posix" else "cls")
        self.ui.mostrar_tablero(tablero.casillas)
        print("\n¡Empate! No quedan más lugares.")
        self.history_manager.guardar("Empate")
