import random
import math


def distribuir_carga() -> tuple:
    zonas = {
        'A': 20,
        'B': 15,
        'C': 10,
        'D': 12,
    }
    carga_actual = {zona: 0 for zona in zonas}
    zonas_desbordadas = set()

    for entrega_num in range(1, 11):
        entrega = random.randint(1, 8)

        if entrega <= 2:
            zona = 'A'
        elif entrega <= 4:
            zona = 'B'
        elif entrega <= 6:
            zona = 'C'
        else:
            zona = 'D'

        limite = zonas[zona]
        nueva_carga = carga_actual[zona] + entrega

        if nueva_carga > limite:
            zonas_desbordadas.add(zona)

        carga_actual[zona] = nueva_carga
        espacio_sobrante = limite - carga_actual[zona]
        espacio_sobrante = math.fmod(espacio_sobrante, limite)

        print(f'Entrega {entrega_num}: zona={zona}, carga={entrega}, espacio sobrante={espacio_sobrante}')

    return carga_actual, zonas_desbordadas


if __name__ == '__main__':
    resultado = distribuir_carga()
    print('Carga final por zona:', resultado[0])
    print('Zonas desbordadas:', resultado[1])
