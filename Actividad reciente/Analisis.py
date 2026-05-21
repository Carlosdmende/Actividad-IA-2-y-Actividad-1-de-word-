def analizar_palabras(lista1, lista2):
    
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    en_ambas = conjunto1.intersection(conjunto2)
    exclusivas_primera = conjunto1.difference(conjunto2)

    print("Palabras en ambas listas:", en_ambas)
    print("Palabras exclusivas de la primera lista:", exclusivas_primera)


if __name__ == "__main__":
    lista_a = ["conjunto", "función", "variable", "python", "mamatripa"]
    lista_b = ["función", "programa", "python", "lista"]
    analizar_palabras(lista_a, lista_b)
