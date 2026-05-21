import random


def encriptar_numeros(numeros: list) -> tuple:
    clave = random.randint(1, 10)
    cifrado = {}
    valores_cifrados = set()

    for numero in numeros:
        if numero % 2 == 0:
            valor = numero + clave
        else:
            valor = numero - clave
        cifrado[numero] = valor
        valores_cifrados.add(valor)

    return clave, valores_cifrados


if __name__ == '__main__':
    lista_original = [4, 7, 2, 9, 10]
    clave, valores_unicos = encriptar_numeros(lista_original)
    print('Clave:', clave)
    print('Lista original:', lista_original)
    print('Valores cifrados únicos:', valores_unicos)
