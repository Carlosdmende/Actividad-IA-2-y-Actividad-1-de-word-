def main():
    inventario = {
        "tiburones de gomita": 10,
        "RX 580": 8,
        "mouse gamer": 5,
        "LINGOTES DE RAM": 12
    }

    print("Simulador de Inventario. Escribe 'salir' para terminar.")
    while True:
        print("\nInventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad}")

        respuesta = input("Producto a vender: ").strip().lower()
        if respuesta == "salir":
            print("Saliendo...")
            break

        if respuesta not in inventario:
            print("Producto no encontrado. Intenta de nuevo.")
            continue

        try:
            cantidad_str = input("Cantidad a vender: ").strip()
            cantidad_vender = int(cantidad_str)
            if cantidad_vender <= 0:
                print("Ingresa un número entero positivo.")
                continue
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue

        if inventario[respuesta] == 0:
            print(f"No hay {respuesta} en stock.")
        elif inventario[respuesta] < cantidad_vender:
            print(f"Stock insuficiente. Solo quedan {inventario[respuesta]} {respuesta}.")
        else:
            inventario[respuesta] -= cantidad_vender
            print(f"Venta realizada: {cantidad_vender} {respuesta}. Quedan {inventario[respuesta]}.")


if __name__ == "__main__":
    main()
