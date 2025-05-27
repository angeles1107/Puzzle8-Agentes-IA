# Puzzle8-Agentes-IA
Este proyecto implementa dos agentes inteligentes capaces de resolver el Puzzle 8 utilizando dos enfoques de búsqueda: uno no informado y otro informado
# Resolución del Puzzle 8 mediante Agentes Inteligentes: Comparación entre BFS y A*

El Puzzle 8 es un problema clásico en inteligencia artificial que consiste en deslizar fichas numeradas en una cuadrícula de 3x3 hasta alcanzar una configuración objetivo. El sistema desarrollado genera tableros aleatorios resolubles, permite elegir el algoritmo a utilizar y muestra el proceso de resolución paso a paso mediante una interfaz gráfica.

El proyecto fue desarrollado en Python y utiliza la biblioteca `pygame` para la visualización interactiva. El usuario puede:

- Generar nuevos puzzles aleatorios
- Seleccionar el algoritmo (BFS o A*)
- Ver la resolución del puzzle en tiempo real
- Consultar estadísticas como nodos expandidos, pasos y tiempo

## Estructura del proyecto

- `main.py`: Archivo principal que ejecuta el programa
- `config.py`: Parámetros de configuración y constantes del sistema
- `puzzle.py`: Representación y validación del estado del puzzle
- `algoritmos.py`: Implementación de los algoritmos BFS y A*
- `interfaz.py`: Interfaz gráfica desarrollada con pygame
- `README.md`: Este archivo


## Ejecución

Antes de ejecutar el programa, asegúrate de tener instalada la biblioteca `pygame`:

```bash
pip install pygame

