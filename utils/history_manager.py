from datetime import datetime
from colorama import Fore, Style

class HistoryManager:

    
    def __init__(self, filename="historial.txt"):
        self.filename = filename
    
    def guardar(self, resultado):

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(self.filename, "a") as archivo:
            archivo.write(f"[{fecha}] {resultado}\n")
    
    def mostrar(self):

        try:
            with open(self.filename, "r") as archivo:
                print(f"\n{Fore.CYAN}--- HISTORIAL DE PARTIDAS ---{Style.RESET_ALL}")
                lineas = archivo.readlines()
                if not lineas:
                    print("El historial está vacío.")
                else:
                    for linea in lineas:
                        print(linea.strip())
        except FileNotFoundError:
            print("\nEl historial aún no existe.")
    
    def borrar(self):

        open(self.filename, "w").close()
        print(f"\n{Fore.YELLOW}Historial borrado.{Style.RESET_ALL}")
    
    def mostrar_estadisticas(self):

        try:
            with open(self.filename, "r") as archivo:
                lineas = archivo.readlines()
                
                if not lineas:
                    print("\nNo hay datos para mostrar estadísticas.")
                    return
                
                victorias_x = 0
                victorias_o = 0
                empates = 0
                
                for linea in lineas:
                    if "Ganador:" in linea and "(X)" in linea:
                        victorias_x += 1
                    elif "Ganador:" in linea and "(O)" in linea:
                        victorias_o += 1
                    elif "Empate" in linea:
                        empates += 1
                
                total = victorias_x + victorias_o + empates
                
                print(f"\n{Fore.CYAN}--- ESTADÍSTICAS ---{Style.RESET_ALL}")
                print(f"Total de partidas: {total}")
                print(f"Victorias X: {victorias_x} ({round(victorias_x/total*100, 1) if total > 0 else 0}%)")
                print(f"Victorias O: {victorias_o} ({round(victorias_o/total*100, 1) if total > 0 else 0}%)")
                print(f"Empates: {empates} ({round(empates/total*100, 1) if total > 0 else 0}%)")
                
        except FileNotFoundError:
            print("\nEl historial aún no existe.")
