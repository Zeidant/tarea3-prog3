# Definir una función para agregar un nuevo estudiante
def agregar_estudiante(registros):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    registros.append({'nombre': nombre, 'edad': edad})

# Definir una función para mostrar todos los estudiantes
def mostrar_estudiantes(registros):
    print("Lista de estudiantes:")
    for estudiante in registros:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

# Programa principal
def main():
    # Inicializar la lista de registros de estudiantes
    estudiantes = []

    # Menú de opciones
    while True:
        print("\n1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(estudiantes)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

# Llamar al programa principal
if __name__ == "__main__":
    main()
