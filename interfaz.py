"""
interfaz.py

Contiene funciones gráficas para mostrar el estado del puzzle en pantalla
usando Pygame, incluyendo el tablero de juego y las estadísticas de ejecución.
"""

import pygame
from config import *

def dibujar_tablero(pantalla, estado, fuente):

    """
    Dibuja el tablero del puzzle 8 en pantalla.
    """

    for i in range(9):
        fila = i // 3
        col = i % 3
        x = col * TAM_CASILLA + 10   # Posición horizontal del recuadro
        y = fila * TAM_CASILLA       # Posición vertical del recuadro
        valor = estado[i]

        if valor != 0:
            # Dibuja el rectángulo con color de casilla si tiene número
            pygame.draw.rect(pantalla, CASILLA_COLOR, (x, y, TAM_CASILLA, TAM_CASILLA))

            # Renderiza el número dentro de la casilla
            texto = fuente.render(str(valor), True, FUENTE_COLOR)
            rect_texto = texto.get_rect(center=(x + TAM_CASILLA // 2, y + TAM_CASILLA // 2))
            pantalla.blit(texto, rect_texto)
        else:
            # Dibuja la casilla vacía (el número 0 representa el hueco)
            pygame.draw.rect(pantalla, FONDO_COLOR, (x, y, TAM_CASILLA, TAM_CASILLA))

        # Dibuja borde negro alrededor de cada casilla
        pygame.draw.rect(pantalla, (0, 0, 0), (x, y, TAM_CASILLA, TAM_CASILLA), 2)

def mostrar_estadisticas(pantalla, fuente_stats, nodos, pasos, tiempo, resuelto):

    """
    Muestra estadísticas de ejecución debajo del tablero.
    """
    if resuelto:
        # Si se resolvió el puzzle, muestra las estadísticas de solución
        texto = f"Nodos: {nodos}   Pasos: {pasos}   Tiempo: {tiempo:.4f}s"
        color = FUENTE_COLOR
    else:
        # Si el puzzle es irresoluble, muestra mensaje en rojo
        texto = "Puzzle irresoluble"
        color = ROJO

    # Renderiza el texto y lo dibuja debajo del tablero
    texto_render = fuente_stats.render(texto, True, color)
    pantalla.blit(texto_render, (10, 310))