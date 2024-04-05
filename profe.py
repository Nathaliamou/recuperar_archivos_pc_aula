#Importar biblioteca random, se utiliza para generar identificadores aleatorios para las bandas.
import random

# Estructuras de datos. Se definen 3 listas vacías: bandas, equipos y programa de actuación, que almacenarán información: 
bandas = []
equipos = []
programa = []

# Definir un contador de ID global
contador_id = 0

# Función para generar un ID único para cada banda
def generar_id():
    global contador_id
    contador_id += 1
    return contador_id

# Funciones
 
# Permite al usuario agregar información sobre una nueva banda.
def agregar_banda():
    id_banda = generar_id()
    nombre = input("Nombre de la banda: ")
    genero = input("Género de la banda: ")
    clasificacion = input("Clasificación (amateur/intermedio/especial): ")

    if clasificacion == "amateur":
        tiempo = int(input("Tiempo de actuación (minutos): "))
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion, "tiempo": tiempo}
    elif clasificacion == "intermedio":
        costo = float(input("Costo de la banda: "))
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion, "costo": costo}
    elif clasificacion == "especial":
        banda = {"id": id_banda, "nombre": nombre, "genero": genero, "clasificacion": clasificacion}
    else:
        print("Clasificación no válida.")
        return
    bandas.append(banda)

#Permite al usuario agregar el nombre de un equipo relacionado con el evento
def agregar_equipo():
    nombre_equipo = input("Nombre del equipo: ")
    equipos.append(nombre_equipo)

#Permite al usuario agregar banda al programa de actuación ingresando su ID.
# Verifica si la banda existe en la lista de bandas y la agrega al programa.
def agregar_programa():
    id_banda = int(input("ID de la banda a agregar al programa: "))
    banda = next((b for b in bandas if b["id"] == id_banda), None)
    if banda:
        programa.append(banda)
    else:
        print("Banda no encontrada.")

#Permite al usuario cancelar una banda del programa ingresando su ID.
# Elimina la banda correspondiente del programa.
def modificar_programa():
    id_banda = int(input("ID de la banda que cancela: "))
    programa[:] = [b for b in programa if b["id"] != id_banda]

#Permite al usuario buscar información detallada sobre una banda ingresando su ID.
# Muestra el nombre, género, clasificación y, si está disponible, el tiempo de actuación o el costo.
def buscar_info():
    id_banda = int(input("ID de la banda a buscar: "))
    banda = next((b for b in bandas if b["id"] == id_banda), None)
    if banda:
        print("Información de la banda:")
        print("ID:", banda["id"])
        print("Nombre:", banda["nombre"])
        print("Género:", banda["genero"])
        print("Clasificación:", banda["clasificacion"])
        if "tiempo" in banda:
            print("Tiempo de actuación:", banda["tiempo"], "minutos")
        elif "costo" in banda:
            print("Costo de la banda:", banda["costo"])
    else:
        print("Banda no encontrada.")

# Función para mostrar las bandas agregadas
def mostrar_bandas():
    print("\n*** Bandas Agregadas ***")
    for banda in bandas:
        print("ID:", banda["id"])
        print("Nombre:", banda["nombre"])
        print("Género:", banda["genero"])
        print("Clasificación:", banda["clasificacion"])
        if "tiempo" in banda:
            print("Tiempo de actuación:", banda["tiempo"], "minutos")
        elif "costo" in banda:
            print("Costo de la banda:", banda["costo"])
        print("------------------------")


# Menú principal
#Un bucle while que muestra un menú de opciones al usuario
while True:
    print("\n*** Menú Principal ***")
    print("1. Agregar banda")
    print("2. Agregar equipo")
    print("3. Agregar banda al programa")
    print("4. Modificar programa (cancelar banda)")
    print("5. Buscar información")
    print("6. Mostrar bandas agregadas")  # Nueva opción para mostrar las bandas agregadas
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_banda()
    elif opcion == "2":
        agregar_equipo()
    elif opcion == "3":
        agregar_programa()
    elif opcion == "4":
        modificar_programa()
    elif opcion == "5":
        buscar_info()
    elif opcion == "6":
        mostrar_bandas()  # Llamada a la función para mostrar las bandas agregadas
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")