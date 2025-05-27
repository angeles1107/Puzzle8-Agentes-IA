"""
config.py

Contiene constantes de configuración para la interfaz del juego.
Define tamaños, colores, el estado meta y los movimientos permitidos del tablero.

"""

# Tamaño de la ventana y del tablero
ANCHOEXTRA = 300
ANCHO = 200 + ANCHOEXTRA
ALTURA_EXTRA = 80
ALTO = 300 + ALTURA_EXTRA
TAM_CASILLA = ANCHOEXTRA // 3

# Colores
FONDO_COLOR = (240, 240, 240)
CASILLA_COLOR = (255, 182, 191)
FUENTE_COLOR = (0, 0, 0)
ROJO = (255, 0, 0)

# Meta
META = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# Diccionario de movimientos válidos según la posición del espacio vacío (índice)
# Cada clave representa la posición del 0, y su valor indica a qué posiciones puede moverse
MOVIMIENTOS = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
