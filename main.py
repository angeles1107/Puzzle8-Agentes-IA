
"""
main.py

Programa principal para ejecutar el puzzle 8 usando una interfaz gráfica con Pygame.
Permite seleccionar entre los algoritmos de búsqueda BFS y A* para resolver el puzzle.
"""

import pygame

from config import *
from puzzle import generar_estado_aleatorio
from algoritmos import bfs, a_estrella
from interfaz import dibujar_tablero, mostrar_estadisticas

def main():
    # Inicializa Pygame
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("8 Puzzle - BFS o A*")

    # Fuentes para el texto
    fuente = pygame.font.Font(None, 60)
    fuente_stats = pygame.font.Font(None, 28)
    fuente_btn = pygame.font.Font(None, 36)

    # Variables del estado
    estado_inicial = generar_estado_aleatorio()
    camino = []
    expandidos = 0
    duracion = 0
    resuelto = False
    pasos = 0
    mostrando_solucion = False
    i = 0
    
    reloj = pygame.time.Clock()

    # Botones
    boton_bfs = pygame.Rect(330, 50, 120, 50)
    boton_astar = pygame.Rect(330, 120, 120, 50)
    boton_nuevo = pygame.Rect(330, 190, 120, 50)
    color_boton = (254, 130, 140)

    corriendo = True
    esperando_click_para_reiniciar = False

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Si ya se resolvió y se hace clic, reinicia para mostrar los botones y el puzzle
                if esperando_click_para_reiniciar:
                    mostrando_solucion = False
                    esperando_click_para_reiniciar = False

                # Si se hace clic en el botón BFS y no se está mostrando solución
                elif boton_bfs.collidepoint(evento.pos) and not mostrando_solucion:
                    camino, expandidos, duracion, resuelto = bfs(estado_inicial)
                    pasos = len(camino) - 1 if resuelto else 0
                    mostrando_solucion = True
                    i = 0

                # Si se hace clic al botón A*  y no se está mostrando solución  
                elif boton_astar.collidepoint(evento.pos) and not mostrando_solucion:
                    camino, expandidos, duracion, resuelto = a_estrella(estado_inicial)
                    pasos = len(camino) - 1 if resuelto else 0
                    mostrando_solucion = True
                    i = 0

                # Si se hace clic al botón Nuevo Puzzle  y no se está mostrando solución  
                elif boton_nuevo.collidepoint(evento.pos) and not mostrando_solucion:
                    estado_inicial = generar_estado_aleatorio()
                    
                    camino = []

                    i = 0

        # Fondo
        pantalla.fill(FONDO_COLOR)

        # Si ya se está mostrando la solución
        if mostrando_solucion and camino:
            if resuelto and i < len(camino):
                # Dibuja paso a paso
                dibujar_tablero(pantalla, camino[i], fuente)
                mostrar_estadisticas(pantalla, fuente_stats, expandidos, pasos, duracion, True)
                i += 1
                pygame.display.flip()
                pygame.time.delay(500)
            elif resuelto and i >= len(camino):
                # Ya terminó de mostrar todos los pasos
                dibujar_tablero(pantalla, camino[-1], fuente)
                mostrar_estadisticas(pantalla, fuente_stats, expandidos, pasos, duracion, True)
                esperando_click_para_reiniciar = True

        elif mostrando_solucion and not resuelto:
            # En el caso de que el puzzle sea irresoluble
            texto = fuente.render("Sin solución", True, ROJO)
            pantalla.blit(texto, texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 20)))
            mostrar_estadisticas(pantalla, fuente_stats, expandidos, 0, duracion, False)
            esperando_click_para_reiniciar = True
        else:
            # Pantalla inicial (antes de resolver)
            dibujar_tablero(pantalla, estado_inicial, fuente)
            texto_info = fuente_stats.render("Selecciona el algoritmo BFS o A* para resolver", True, FUENTE_COLOR)
            pantalla.blit(texto_info, (10, 310))

        # Se dibuja los botones si no se está mostrando solución

        if not mostrando_solucion and not esperando_click_para_reiniciar:
            pygame.draw.rect(pantalla, color_boton, boton_bfs)
            pantalla.blit(fuente_btn.render("BFS", True, (0, 0, 0)), boton_bfs.move(35, 15))

            pygame.draw.rect(pantalla, color_boton, boton_astar)
            pantalla.blit(fuente_btn.render("A*", True, (0, 0, 0)), boton_astar.move(50, 15))

            pygame.draw.rect(pantalla, (164, 125, 171), boton_nuevo)
            pantalla.blit(fuente_btn.render("Nuevo", True, (255, 255, 255)), boton_nuevo.move(23, 12))

        # Mostrar mensaje de continuar si ya terminó la animación
        if esperando_click_para_reiniciar:
            if resuelto:
                texto_continuar = fuente_stats.render("¡Puzzle resuelto! Haz clic para continuar...", True, (0, 150, 0))
            else:
                texto_continuar = fuente_stats.render("Haz clic para continuar...", True, (0, 0, 0))
            pantalla.blit(texto_continuar, (10, 340))

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()