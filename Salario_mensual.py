def main():
    numeros = []  # Inicializar un arreglo vacío para almacenar los números

    while True:
        print("\n--- Menú ---")
        print("1. Ingresar salario mensual")
        print("2. Ingresar ingresos extras mensuales")
        print("3. Ingresar gastos mensuales")
        print("4. Calcular ahorro anual")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            salario = float(input("Ingrese su salario mensual en PYG: "))
            numeros.append(salario)  # Agregar el salario al arreglo
            print("Salario ingresado correctamente.")
        elif opcion == "2":
            ingresos_extras = float(input("Ingrese el monto de los ingresos extras mensuales en PYG: "))
            numeros.append(ingresos_extras)  # Agregar ingresos extra al arreglo
            print("Ingresos extras ingresados correctamente.")
        elif opcion == "3":
            gastos = float(input("Ingrese el valor de los gastos mensuales en PYG: "))
            numeros.append(gastos)  # Agregar gastos al arreglo
            print("Gastos ingresados correctamente.")
        elif opcion == "4":
            try:
                salario = numeros[0]
                ingresos_extras = numeros[1]
                gastos = numeros[2]
                ahorro_anual = (salario + ingresos_extras - gastos) * 12
                print(f"El ahorro anual es de: {ahorro_anual} PYG")
            except NameError:
                print("Error: Debe ingresar primero todos los datos.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
