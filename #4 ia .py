import random
import math


def simular_particulas() -> dict:
    radios = [random.randint(1, 10) for _ in range(10)]
    particulas = {}
    areas_unicas = set()

    for indice, radio in enumerate(radios, start=1):
        area = math.pi * (radio ** 2)
        particulas[indice] = (radio, area)
        areas_unicas.add(area)

    return {
        'radios': radios,
        'particulas': particulas,
        'areas_unicas': areas_unicas,
    }


if __name__ == '__main__':
    resultado = simular_particulas()
    print('Radios:', resultado['radios'])
    print('Partículas (índice: (radio, área)):', resultado['particulas'])
    print('Áreas únicas:', resultado['areas_unicas'])
