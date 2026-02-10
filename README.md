# Trabajo Práctico: Desarrollo Guiado por Pruebas (TDD) en Python

## Objetivo
El objetivo de este trabajo práctico es aprender y aplicar el Desarrollo Guiado por Pruebas (TDD) en Python utilizando el módulo `unittest`, alcanzando una cobertura de código superior al 90%. Deberás implementar una aplicación completa siguiendo estrictamente el ciclo de TDD: escribir pruebas primero, luego el código mínimo necesario para pasar las pruebas, y refactorizar manteniendo la funcionalidad, aplicando principios SOLID y separando claramente la lógica del juego de la interfaz de usuario.

## Descripción del Proyecto
Implementarás un **juego de Ta-Te-Ti (Tres en Línea)** completo, con las siguientes características:

### Funcionalidades Requeridas
- **Lógica del Juego**:
  - Tablero de 3x3
  - Dos jugadores (humano vs humano, humano vs IA)
  - Detección de victorias, empates y movimientos inválidos
  - Modos de juego: PvP (jugador vs jugador), PvIA (jugador vs IA simple), IA vs IA
  - Historial de partidas
  - Estadísticas de victorias/derrotas

- **Interfaz de Usuario** (separada de la lógica):
  - Interfaz de consola para entrada/salida
  - Menú principal para seleccionar modos de juego
  - Visualización clara del tablero
  - Mensajes informativos durante el juego

- **IA**:
  - Implementación completa del algoritmo Minimax con poda alfa-beta para eficiencia
  - Función de evaluación para estados del tablero
  - Profundidad de búsqueda configurable
  - Modo de dificultad: fácil (aleatorio), medio (minimax limitado), difícil (minimax completo)
  - Pruebas unitarias para la lógica de IA

### Principios SOLID a Aplicar
- **S (Single Responsibility)**: Cada clase debe tener una única responsabilidad (ej. Board maneja el tablero, Game maneja la lógica del juego, UI maneja la interfaz)
- **O (Open-Closed)**: El código debe estar abierto a extensión pero cerrado a modificación (ej. agregar nuevos tipos de IA sin cambiar el código existente)
- **L (Liskov Substitution)**: Subclases deben ser sustituibles por sus padres
- **I (Interface Segregation)**: Interfaces específicas en lugar de generales
- **D (Dependency Inversion)**: Depender de abstracciones, no de concretos

## Requisitos Técnicos
- **Lenguaje**: Python 3.x
- **Framework de Pruebas**: `unittest`
- **Cobertura de Código**: Debe superar el 90% de cobertura de código, medida con `coverage.py`
- **Organización del Código**: Uso de módulos y paquetes Python para una estructura clara y modular
- **Estructura del Proyecto**:
  ```
  tictactoe/
  ├── game/
  │   ├── __init__.py
  │   ├── board.py              # Lógica del tablero
  │   ├── game.py               # Lógica principal del juego
  │   ├── player.py             # Clases de jugadores (humano, IA)
  │   └── ai.py                 # Implementación de IA
  ├── ui/
  │   ├── __init__.py
  │   └── console_ui.py         # Interfaz de consola
  ├── tests/
  │   ├── __init__.py
  │   ├── test_board.py
  │   ├── test_game.py
  │   ├── test_player.py
  │   └── test_ai.py
  ├── main.py                   # Punto de entrada
  ├── requirements.txt          # Dependencias
  └── README.md                 # Este archivo
  ```

## Metodología TDD
Sigue el ciclo Red-Green-Refactor:

1. **Red**: Escribe una prueba que falle (para una funcionalidad que aún no existe)
2. **Green**: Implementa el código mínimo necesario para que la prueba pase
3. **Refactor**: Mejora el código sin cambiar su comportamiento, asegurándote de que todas las pruebas sigan pasando

### Pasos Sugeridos
1. Comienza con la lógica del tablero (`board.py` y `test_board.py`)
2. Implementa la lógica del juego (`game.py` y `test_game.py`)
3. Agrega jugadores y IA (`player.py`, `ai.py` y sus tests)
4. Implementa la UI separadamente (`console_ui.py`)
5. Integra todo en `main.py`
6. Ejecuta las pruebas con `python -m unittest`
7. Mide la cobertura con `coverage run -m unittest` y `coverage report`
8. Asegúrate de que la cobertura sea >90%

## Ejemplos de Uso
```python
from game.game import TicTacToeGame
from game.player import HumanPlayer, AIPlayer
from ui.console_ui import ConsoleUI

# Crear juego
game = TicTacToeGame()
ui = ConsoleUI()

# Configurar jugadores
player1 = HumanPlayer("X")
player2 = AIPlayer("O")

# Jugar
game.play(player1, player2, ui)
```

## Criterios de Evaluación
- Correcta implementación del ciclo TDD
- Aplicación de principios SOLID
- Separación clara entre lógica y UI
- Todas las pruebas pasan
- Cobertura de código >90%
- Código limpio, modular y bien estructurado
- Manejo adecuado de errores y casos edge
- Documentación clara (docstrings y comentarios)
- Funcionalidad completa del juego

## Recursos Adicionales
- [Documentación oficial de unittest](https://docs.python.org/3/library/unittest.html)
- [Introducción a TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- [Principios SOLID](https://en.wikipedia.org/wiki/SOLID)
- [Coverage.py](https://coverage.readthedocs.io/)