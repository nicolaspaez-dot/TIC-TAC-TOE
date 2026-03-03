"""
Punto de entrada del juego de Ta-Te-Ti.
Solo instancia los componentes y ejecuta el loop principal.
"""
from utils.history_manager import HistoryManager
from ui.menu import MenuManager
from game.game_controller import GameController


def main():
   
    history = HistoryManager("historial.txt")
    menu = MenuManager(history)
    controller = GameController(history)
    
    
    ejecutando = True
    
    while ejecutando:
        menu.mostrar_menu_principal()
        modo = menu.obtener_opcion()
        
        if modo == "8":
            break
        
        if modo == "6":
            menu.mostrar_historial()
            continue
        
        if modo == "7":
            menu.mostrar_estadisticas()
            continue
        
        config = menu.configurar_partida(modo)
        
        if config is None:
            continue  
        
        nombre_x, nombre_o, bot_x, bot_o = config
        
        controller.jugar_partida(nombre_x, nombre_o, bot_x, bot_o)

if __name__ == "__main__":
    main()