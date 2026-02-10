import os
from colorama import Fore, Style
from game.player import AIPlayer

class MenuManager:
    
    def __init__(self, history_manager):
        self.history_manager = history_manager
    
    def mostrar_menu_principal(self):
        os.system("clear" if os.name == "posix" else "cls")
        print(f"{Fore.RED}-.- Tic Tac Toe -.-{Style.RESET_ALL}")
        print("1. Humano vs Humano")
        print("2. Humano vs Ricochet (Fácil)")
        print("3. Humano vs Ricochet (Medio)")
        print("4. Humano vs Ricochet (Difícil - Minimax)")
        print("5. IA vs IA (Modo Espectador)")
        print("6. Ver Historial")
        print("7. Ver Estadísticas")
        print("8. Salir")
    
    def obtener_opcion(self):
        return input("\nElegí una opción: ")
    
    def mostrar_historial(self):
        os.system("clear" if os.name == "posix" else "cls")
        self.history_manager.mostrar()
        print("\n1. Borrar historial | Otra tecla para volver")
        if input("Opción: ") == "1":
            self.history_manager.borrar()
        input("\nPresioná Enter para continuar...")
    
    def mostrar_estadisticas(self):
        os.system("clear" if os.name == "posix" else "cls")
        self.history_manager.mostrar_estadisticas()
        input("\nPresioná Enter para continuar...")
    
    def configurar_partida(self, modo):

        bot_x = None
        bot_o = None
        
        if modo == "1":
            nombre_x = input("\nNombre del Jugador X: ")
            nombre_o = input("Nombre del Jugador O: ")
        elif modo == "2":
            nombre_x = input("\nTu nombre (X): ")
            nombre_o = "Ricochet (Fácil)"
            bot_o = AIPlayer("O", dificultad="normal")
        elif modo == "3":
            nombre_x = input("\nTu nombre (X): ")
            nombre_o = "Ricochet (Medio)"
            bot_o = AIPlayer("O", dificultad="medio")
        elif modo == "4":
            nombre_x = input("\nTu nombre (X): ")
            nombre_o = "Ricochet (Tryhard)"
            bot_o = AIPlayer("O", dificultad="dificil")
        elif modo == "5":
            nombre_x = "Bot Alpha (X)"
            nombre_o = "Bot Omega (O)"
            bot_x = AIPlayer("X", dificultad="dificil")
            bot_o = AIPlayer("O", dificultad="dificil")
        else:
            return None  
        
        return (nombre_x, nombre_o, bot_x, bot_o)
