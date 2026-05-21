def operaciones_numeros(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division_entera = a // b if b != 0 else None
    return (suma, resta, multiplicacion, division_entera)

if __name__ == "__main__":
    num1 = 10
    num2 = 3
    suma, resta, multiplicacion, division_entera = operaciones_numeros(num1, num2)
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División entera:", division_entera)
