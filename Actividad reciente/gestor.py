def main():
	estudiantes = {
		"jesus": [8.5, 9.0, 7.5],
		"diego": [6.0, 7.0, 8.0],
		"jongervy": [9.5, 8.5, 10.0]
	}

	for nombre, notas in estudiantes.items():
		promedio = sum(notas) / len(notas)
		print(f"{nombre}: Promedio = {promedio:.2f}")


if __name__ == "__main__":
	main()