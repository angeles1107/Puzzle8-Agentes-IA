import time
import heapq
from collections import deque
from puzzle import es_resoluble, reconstruir_camino, generar_vecinos, heuristica_manhattan
from config import META

def bfs(inicial):

    """
    Algoritmo de búsqueda en anchura (Breadth-First Search) para resolver el puzzle 8.
    Busqueda No Informada
    """
    #Verifica si el estado inicial es resoluble
    if not es_resoluble(inicial):
        return None, 0, 0.0, False

    visitados = set()         # Conjunto para no procesar un estado dos veces
    cola = deque()
    padres = {}          # diccionario para reconstruir el camino

    #Encola el estado inicial, lo marca como visitado y registra que no tiene padre(la raiz del arbol de busqueda)
    cola.append(inicial)
    visitados.add(inicial)
    padres[inicial] = None

    nodos_expandidos = 0 # Contador de nodos procesados
    inicio = time.time()

    while cola:
        actual = cola.popleft()    # Sacamos el primer estado en la cola
        nodos_expandidos += 1      # Va contabilizando la expansión

        # Si alcanza la meta, entonces se reconstruye el camino y devolvemos resultados
        if actual == META:
            fin = time.time()
            camino = reconstruir_camino(padres, actual)
            return camino, nodos_expandidos, fin - inicio, True

        #Genera y procesa vecinos del estado actual (cada estado alcanzable moviendo la ficha 0)
        for vecino in generar_vecinos(actual):
            #Si un vecino no se ha visto 
            if vecino not in visitados:
                padres[vecino] = actual   #Guarda quien lo generó
                visitados.add(vecino)    # Se marca como visitado
                cola.append(vecino)  # Encolarlo para explorarlo más tarde
    
    #Si la cola se vacía sin encontrar la meta entonces no hay solución
    fin = time.time()
    return None, nodos_expandidos, fin - inicio, False

def a_estrella(inicial):

    """
    Algoritmo de Búsqueda A* (A estrella) para resolver el puzzle 8.
    Busqueda Informada: usa heurística (distancia Manhattan) para
    priorizar los estados que parecen más prometedores.
    
    """
    if not es_resoluble(inicial):
        return None, 0, 0.0, False

    abiertos = []   # Cola de prioridad (heap) con los estados por explorar
    heapq.heappush(abiertos, (heuristica_manhattan(inicial), 0, inicial))  # (f = g + h, g, estado)
    padres = {inicial: None}    # Diccionario de padre de cada estado
    costos = {inicial: 0}       # Costos acumulados g(n) desde el inicio
    visitados = set()           # Estados que ya fueron expandidos

    nodos_expandidos = 0        # Contador de nodos explorados
    inicio = time.time()

    while abiertos:

        # Se extrae el estado con menor prioridad f = g + h
        _, g_actual, actual = heapq.heappop(abiertos)
        nodos_expandidos += 1

         # Si llegamos al estado meta, se reconstruye el camino y retornamos
        if actual == META:
            fin = time.time()
            camino = reconstruir_camino(padres, actual)
            return camino, nodos_expandidos, fin - inicio, True

         # Marca este estado como visitado
        visitados.add(actual)

        # Expandir vecinos del estado actual
        for vecino in generar_vecinos(actual):
            nuevo_costo = g_actual + 1

            # Solo actualiza si el vecino es nuevo o encontramos una mejor ruta
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica_manhattan(vecino)  # f = g + h
                heapq.heappush(abiertos, (prioridad, nuevo_costo, vecino))  # Inserta al vecino en la cola de prioridad abiertos, con su prioridad f, su costo g, y su estado
                padres[vecino] = actual       #Para reconstuir el camino 
    
    fin = time.time()
    return None, nodos_expandidos, fin - inicio, False
