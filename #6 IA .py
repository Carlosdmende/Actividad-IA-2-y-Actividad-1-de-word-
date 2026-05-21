import random
import math


def simular_temperaturas() -> dict:
    estaciones = {
        'Norte': tuple(random.randint(-10, 25) for _ in range(5)),
        'Sur': tuple(random.randint(5, 30) for _ in range(5)),
        'Este': tuple(random.randint(0, 35) for _ in range(5)),
        'Oeste': tuple(random.randint(-5, 28) for _ in range(5)),
    }

    promedios = {}
    anomalías = set()

    for estacion, temperaturas in estaciones.items():
        suma = 0
        for temp in temperaturas:
            suma += temp
        promedio = math.floor(suma / len(temperaturas))
        promedios[estacion] = promedio

        for temp in temperaturas:
            if temp <= -5 or temp >= 30:
                anomalías.add((estacion, temp))

    return {
        'estaciones': estaciones,
        'promedios': promedios,
        'anomalías': anomalías,
    }


if __name__ == '__main__':
    datos = simular_temperaturas()
    print('Temperaturas por estación:')
    for estacion, temperaturas in datos['estaciones'].items():
        print(f'  {estacion}: {temperaturas}')
    print('Promedios truncados:', datos['promedios'])
    print('Anomalías detectadas:', datos['anomalías'])
