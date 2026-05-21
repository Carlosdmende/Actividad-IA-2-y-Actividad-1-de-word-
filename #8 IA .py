import math


def analizar_ips() -> dict:
    ips = [
        (10, 0, 0, 1),
        (192, 168, 1, 100),
        (172, 16, 0, 5),
        (203, 0, 113, 8),
    ]
    prohibidos = {0, 127, 255}
    clasificacion = {}

    for ip in ips:
        invalido = any(octeto in prohibidos for octeto in ip)
        peso = sum(ip)
        peso_log = math.log(peso) if peso > 0 else 0

        if invalido:
            estado = 'inválida'
        elif ip[0] >= 224:
            estado = 'multicast'
        elif ip[0] == 10 or ip[0] == 172 or ip[0] == 192:
            estado = 'privada'
        else:
            estado = 'pública'

        clasificacion[ip] = {
            'estado': estado,
            'peso': peso,
            'peso_log': peso_log,
        }

    return clasificacion


if __name__ == '__main__':
    resultado = analizar_ips()
    for ip, datos in resultado.items():
        print(f'IP {ip}:', datos)
