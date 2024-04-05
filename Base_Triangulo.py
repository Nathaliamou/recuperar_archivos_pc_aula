def calcular_base(area, altura):
    # Calcular la base del triángulo utilizando la fórmula: base = (2 * área) / altura
    base = (2 * area) / altura
    return base

def main():
    numeros = []  # Inicializar un arreglo vacío para almacenar los números
    
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar base del triángulo")
        print("2. Ingresar altura del triángulo")
        print("3. Calcular área del triángulo")
        print("4. Mostrar números ingresados y el área del Triángulo")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            base = float(input("Ingrese la base del triángulo: "))
            numeros.append(base)  # Agregar la base al arreglo
            print("Base ingresada correctamente.")

        elif opcion == "2":
            if len(numeros) < 1:
                print("Error: Debe ingresar primero la base.")
            else:
                altura = float(input("Ingrese la altura del triángulo: "))
                numeros.append(altura)  # Agregar la altura al arreglo
                print("Altura ingresada correctamente.")

        elif opcion == "3":
            if len(numeros) < 2:
                print("Error: Debe ingresar la base y la altura primero.")
            else:
                base = numeros[0]
                altura = numeros[1]
                area = (base * altura) /2
                print(f"El Área del triángulo es: {area}")

        elif opcion == "4":
            if len(numeros) < 2:
                print("No se han ingresado tanto la base como la altura aún.")
            else:
                base = numeros[0]
                altura = numeros[1]
                area = (base * altura) / 2
                print(f"Números ingresados: Base: {base}, Altura: {altura}. El área del triángulo es: {area}")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor ingrese una opción válida.")

if __name__ == "__main__":
    main()
