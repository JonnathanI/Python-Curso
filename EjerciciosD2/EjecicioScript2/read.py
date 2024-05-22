# Función para leer los colaboradores desde el archivo
def leer_colaboradores(archivo):
    try:
        with open(archivo, 'r') as file:
            colaboradores = file.read().splitlines()
        return colaboradores
    except FileNotFoundError:
        return []

# Función para imprimir los colaboradores
def imprimir_colaboradores(colaboradores, num=5):
    if len(colaboradores) == 0:
        print("No hay colaboradores en la lista.")
    else:
        for i, colaborador in enumerate(colaboradores[:num]):
            print(f"{i+1}. {colaborador}")

# Función para agregar un nuevo colaborador
def agregar_colaborador(archivo, colaborador):
    colaboradores = leer_colaboradores(archivo)
    if len(colaboradores) >= 15:
        print("No se puede agregar más colaboradores, la lista está llena.")
    else:
        with open(archivo, 'a') as file:
            file.write(colaborador + '\n')
        print(f"Colaborador {colaborador} agregado con éxito.")

# Función principal que gestiona la lógica del script
def main():
    archivo = 'colaboradores.txt'
    colaboradores = leer_colaboradores(archivo)

    # Solicitar al usuario la acción a realizar
    while True:
        print("\nOpciones:")
        print("1. Ver colaboradores")
        print("2. Agregar colaborador")
        print("3. Salir")
        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == '1':
            num = input("¿Cuántos colaboradores desea ver? (presione Enter para ver los primeros 5): ")
            num = int(num) if num.isdigit() else 5
            imprimir_colaboradores(colaboradores, num)
        elif opcion == '2':
            nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ")
            agregar_colaborador(archivo, nuevo_colaborador)
            colaboradores = leer_colaboradores(archivo)  # Actualizar la lista de colaboradores
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
