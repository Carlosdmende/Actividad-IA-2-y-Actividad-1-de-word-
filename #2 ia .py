import random


def generar_ganadores() -> tuple:
    ganadores = set()
    while len(ganadores) < 3:
        ganadores.add(random.randint(1, 20))
    return tuple(ganadores)


def calcular_premio(aciertos: int, intentos: int) -> int:
    if aciertos == 3:
        return 1000 * intentos
    elif aciertos == 2:
        return 500 * (intentos // 2)
    elif aciertos == 1:
        return 100 * (intentos // 3)
    else:
        return 0


def simular_sorteo(numeros_usuario: list) -> dict:
    ganadores = generar_ganadores()
    aciertos = len(set(numeros_usuario) & set(ganadores))
    premio = calcular_premio(aciertos, len(numeros_usuario))

    return {
        'ganadores': ganadores,
        'numeros_usuario': numeros_usuario,
        'aciertos': aciertos,
        'premio': premio,
    }


if __name__ == '__main__':
    # Ejemplo fijo de 3 números del usuario
    usuario = [3, 7, 15]
    resultado = simular_sorteo(usuario)
    print('Números ganadores:', resultado['ganadores'])
    print('Números del usuario:', resultado['numeros_usuario'])
    print('Aciertos:', resultado['aciertos'])
    print('Premio:', resultado['premio'])
