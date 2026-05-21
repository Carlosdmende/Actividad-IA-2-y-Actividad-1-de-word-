import random

numeros = [random.randint(1, 50) for _ in range(15)]

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Numeros:", numeros)
print("Pares parrosos:", pares)
print("Impares imparry:", impares)
