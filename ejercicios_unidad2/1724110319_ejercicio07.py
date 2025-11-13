# Desarrolle un programa en Python que simule la atención a clientes en una fila de un banco, 
# los clientes llegan y se agregan al final de la cola y el cajero los atiende en el mismo orden en el que llegaron.
# Hay que crear una cola vacía la cual se puede representar con una lista.
# El programa deberá mostrar un menú con las siguientes opciones:

# A) Agregar clientes a la cola
# B) Atender al cliente
# C) Mostrar la cola actual 
# D) Salir 

# Cada vez que se agregue un cliente, el programa deberá solicitar su nombre. Al atender un cliente, se debe eliminar al primer 
# cliente de la cola y mostrar su nombre con una etiqueta de cliente atendido.
# Si se intenta atender cuando la cola está vacía, el programa debe mostrar un mensaje apropiado. 
# Mostrar la cola actual en cada iteración.

cola = []

while True:
    print("\nA) Agregar cliente")
    print("B) Atender cliente")
    print("C) Mostrar cola")
    print("D) Salir")

    opcion = input("Elige una opción: ").upper()

    if opcion == "A":
        nombre = input("Nombre del cliente:")
        cola.append(nombre)
        print(f"Cliente '{nombre}' agregado a la cola.")

    elif opcion == "B":
        if cola:
            print(f"Cliente atendido: {cola.pop(0)}")
        else:
            print("No hay clientes en la cola para atender.")

    elif opcion == "C":
        print("\nCola Actual")
        if len(cola) == 0:
            print("No hay clientes en espera.")
        else:
            for i, cliente in enumerate(cola, start=1):
                print(f"{i}. {cliente}")

    elif opcion == "D":
        print("Saliendo del programa")
        break

    else:
        print("Opción no válida, intenta de nuevo.")