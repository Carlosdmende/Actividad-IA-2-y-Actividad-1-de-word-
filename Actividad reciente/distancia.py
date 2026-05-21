import random
import math


def distancia_euclidiana(p1: tuple, p2: tuple) -> float:
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	return math.sqrt(dx * dx + dy * dy)


if __name__ == "__main__":
	punto1 = (random.randint(0, 10), random.randint(0, 10))
	punto2 = (random.randint(0, 10), random.randint(0, 10))
	distancia = distancia_euclidiana(punto1, punto2)
	print(f"Punto 1: {punto1}")
	print(f"Punto 2: {punto2}")
	print(f"Distancia euclidiana: {distancia}")
