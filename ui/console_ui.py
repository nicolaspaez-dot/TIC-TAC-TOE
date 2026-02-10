from colorama import Fore, Style, init


init(autoreset=True)

class ConsoleUI:
    def pedir_jugada(self, nombre):
        while True:
            mensaje = f"{Fore.GREEN}{nombre}{Fore.WHITE}, elegí una posición (1-9): {Style.RESET_ALL}"
            entrada = input(mensaje)
        
            if not entrada.isdigit():
                print(f"{Fore.RED}¡Error! '{entrada}' no es un número válido.{Style.RESET_ALL}")
                continue
            
                
            posicion = int(entrada)
            if 1 <= posicion <= 9:
                return posicion - 1  # Devolvemos 0-8 para que el Tablero lo entienda
            else:
                print(f"{Fore.YELLOW}¡Ojo! El número tiene que estar entre 1 y 9.{Style.RESET_ALL}")
    
    def mostrar_tablero(self, casillas):
        print("\n")

        casillas_coloreadas = []
        
        for ficha in casillas:
            if ficha == "X":
                casillas_coloreadas.append(f"{Fore.YELLOW}X{Style.RESET_ALL}")

            elif ficha == "O":
                casillas_coloreadas.append(f"{Fore.BLUE}O{Style.RESET_ALL}")

            else:
                casillas_coloreadas.append(f"{Fore.WHITE}-{Style.RESET_ALL}")
       
        for i in range(0, 9, 3):
            fila = casillas_coloreadas[i:i+3]
            print(f" {fila[0]} | {fila[1]} | {fila[2]} ")
            if i < 6:
                print("-----------")
        print("\n")