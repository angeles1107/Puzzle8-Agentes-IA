"""
puzzle.py

Contiene las funciones esenciales para manipular y analizar estados del puzzle 8,
incluyendo la verificación de resolubilidad, generación de vecinos, creación de 
estados aleatorios, reconstrucción de caminos y cálculo de heurística.

"""

from config import META, MOVIMIENTOS
import random

def contar_inversiones(estado):

    """
    Cuenta el número de inversiones en un estado del puzzle.
    Una inversión ocurre cuando un número mayor esta primero que otro menor en la secuencia.

    Parámetro:
        estado (tuple): Estado actual del puzzle.

    Retorna:
        int: Número de inversiones.
    """

    inversos = 0
    lista = [x for x in estado if x != 0] # se crea una lista con todos los valores del estado excepto el 0 (que representa el espacio vacío)
    
    # Recorrer todos los pares posibles de elementos en la lista
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            
            # Si un número mayor aparece antes que uno menor, se cuenta una inversión
            if lista[i] > lista[j]:
                inversos += 1

    return inversos

# Cálculo de la paridad del estado meta, si el número de inversiones es par o impar
PARIDAD_META = contar_inversiones(META) % 2

def es_resoluble(estado):

    """
    Verifica si un estado del puzzle es resoluble.
    """
    contar = contar_inversiones(estado)
    return contar % 2 == PARIDAD_META

def generar_vecinos(estado):

    """
    Genera todos los estados vecinos posibles a partir de un estado actual.

    Parámetro:
        estado (tuple): Estado actual del puzzle.

    Retorna:
        list[tuple]: Lista de estados vecinos que son los movimientos válidos del 0.
    """

    vecinos = []
    idx_cero = estado.index(0)

    # Recorre todas las posiciones a las que el 0 puede moverse desde su ubicación actual
    for mov in MOVIMIENTOS[idx_cero]:
        nuevo = list(estado)             # copia del estado actual para modificarlo
        nuevo[idx_cero], nuevo[mov] = nuevo[mov], nuevo[idx_cero]  # lo que hace es intercambiar el 0 con la ficha ubicada en la posición del movimiento permitido
        
        # Se convierte la lista modificada a tupla y la agregamos a la lista de vecinos
        vecinos.append(tuple(nuevo))
    return vecinos

def generar_estado_aleatorio():
    
    """
    Genera un estado aleatorio del puzzle que sea resoluble
    y diferente del estado meta
    """
    while True:
        estado = list(META)
        random.shuffle(estado)
        estado_tuple = tuple(estado)
        if estado_tuple != META and es_resoluble(estado_tuple):
            return estado_tuple

def reconstruir_camino(padres, estado_final):

    """
    Reconstruye el camino desde el estado inicial hasta el estado final
    usando el diccionario de padres.

    Parámetros:
        padres (dict): Diccionario de padres con claves como estados y
                       valores como el estado anterior.
        estado_final (tuple): Estado destino a reconstruir.

    Retorna:
        list[tuple]: Lista de estados desde el inicial al final.
    """
    camino = []
    actual = estado_final  # Para comenzar desde el estado final y asi ir hacia atrás usando el diccionario de padres 
    
    # Recorre los padres hasta llegar al estado inicial donde su padre es None
    while actual is not None:  
        camino.append(actual)  # Se añade el estado actual al camino
        actual = padres[actual] # lo que hace es avanzar hacia atrás al padre del estado actual
    camino.reverse()  # Para invertir la lista y que quede de inicio a fin
    return camino

def heuristica_manhattan(estado):

    """
    Calcula la heurística de distancia Manhattan entre el estado actual
    y el estado meta. La suma de distancias entre cada ficha y su posición objetivo sin incluir el 0 (casilla vacia)

    """    

    distancia = 0

    for i, valor in enumerate(estado):
        if valor != 0:
            fila_actual, col_actual = divmod(i, 3)  # Calcula fila y columna actual del valor
            fila_meta, col_meta = divmod(META.index(valor), 3)  # Busca dónde debería estar en el estado META
            distancia += abs(fila_actual - fila_meta) + abs(col_actual - col_meta) # Suma la distancia entre ambos

    return distancia
