import random
import math

def generar_muestras(n: int) -> dict:
    """Genera n números aleatorios, elimina duplicados y calcula la raíz cuadrada del máximo."""
    lista = [random.randint(0, 100) for _ in range(n)]
    conjunto = set(lista)
    raiz_cuadrada_maxima = math.sqrt(max(conjunto)) if conjunto else 0

    return {
        'lista': lista,
        'conjunto': conjunto,
        'raiz_cuadrada_maxima': raiz_cuadrada_maxima,
    }

if __name__ == '__main__':
    resultado = generar_muestras(10)
    print('Lista:', resultado['lista'])
    print('Conjunto sin duplicados:', resultado['conjunto'])
    print('Raíz cuadrada del máximo:', resultado['raiz_cuadrada_maxima'])
