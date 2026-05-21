import random

numero_secreto = random.randint(1, 10)
intentos = 3

print("adiviname el número entre el 1 y 10. Tenei 3 intentos si perdei papi un matote.")

for intento in range(1, intentos + 1):
    try:
        respuesta = int(input(f"Intento {intento}: "))
    except ValueError:
        print("dios mio poneme un numero bien.")
        continue

    if respuesta == numero_secreto:
        print("jackpot")
        break
    else:
        print("Fallaste.")
        if intento < intentos:
            print("dale otra vez")
        else:
            print(f"salao no me digai mas. El número e {numero_secreto}.")
