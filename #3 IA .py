import random
import math


def crear_catalogo() -> dict:
    productos = ('Camiseta', 'Zapatos', 'Gorra', 'Mochila', 'Reloj')
    precios = {}

    for producto in productos:
        precio = random.randint(10, 80)
        if precio > 50:
            precio += precio * 0.15
        precio = math.ceil(precio)
        precios[producto] = precio

    precios_finales = set(precios.values())

    return {
        'productos': productos,
        'precios': precios,
        'precios_finales': precios_finales,
    }


if __name__ == '__main__':
    catalogo = crear_catalogo()
    print('Productos:', catalogo['productos'])
    print('Precios:', catalogo['precios'])
    print('Precios finales únicos:', catalogo['precios_finales'])
