import random
import math


def combate_turnos() -> tuple:
    jugador = {'HP': 100, 'Defensa': 3}
    enemigo = {'HP': 80, 'Defensa': 2}
    historial_daño = []
    turno = 1

    while jugador['HP'] > 0 and enemigo['HP'] > 0:
        if turno % 2 == 1:
            atacante, defensor = jugador, enemigo
            nombre = 'Jugador'
        else:
            atacante, defensor = enemigo, jugador
            nombre = 'Enemigo'

        daño_base = random.randint(5, 20)
        mitigación = math.ceil(daño_base / defensor['Defensa'])
        daño_final = max(0, daño_base - mitigación)
        defensor['HP'] = max(0, defensor['HP'] - daño_final)

        historial_daño.append((nombre, daño_base, mitigación, daño_final, defensor['HP']))
        turno += 1

    ganador = 'Jugador' if enemigo['HP'] == 0 else 'Enemigo'
    return ganador, tuple(historial_daño)


if __name__ == '__main__':
    ganador, historial = combate_turnos()
    print('Ganador:', ganador)
    print('Historial de daño:')
    for registro in historial:
        print('  ', registro)
