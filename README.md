

### Funcionalidades 
- **Lógica del Juego**:
  - Tablero de 3x3
  - Dos jugadores (humano vs humano, humano vs IA)
  - Detección de victorias, empates y movimientos inválidos
  - Modos de juego: PvP (jugador vs jugador), PvIA (jugador vs IA simple), IA vs IA
  - Historial de partidas
  - Estadísticas de victorias/derrotas

- **Interfaz de Usuario**:
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

## Técnicos
- **Lenguaje**: Python 3.x
- **Framework de Pruebas**: `unittest`
- **Cobertura de Código**: Debe superar el 90% de cobertura de código, medida con `coverage.py`
- **Organización del Código**: Uso de módulos y paquetes Python para una estructura clara y modular
- **Estructura del Proyecto**:
  
