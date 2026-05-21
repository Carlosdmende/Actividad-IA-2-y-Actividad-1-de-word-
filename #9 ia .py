import random
import math


def calcular_distancias() -> dict:
    origen = (0, 0)
    destinos = [(random.randint(-20, 20), random.randint(-20, 20)) for _ in range(5)]
    distancias = set()
    mapa = {}

    for destino in destinos:
        distancia = math.hypot(destino[0] - origen[0], destino[1] - origen[1])
        mapa[destino] = distancia
        distancias.add(distancia)

    return {
        'origen': origen,
        'destinos': destinos,
        'distancias_unicas': distancias,
        'mapa': mapa,
    }


if __name__ == '__main__':
    resultado = calcular_distancias()
    print('Origen:', resultado['origen'])
    print('Destinos:', resultado['destinos'])
    print('Distancias únicas:', resultado['distancias_unicas'])
    print('Mapa origen-destino:', resultado['mapa'])
