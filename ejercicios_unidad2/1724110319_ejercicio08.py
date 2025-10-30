# Cree un programa en python que simule la atención de personas que hacen fila para comprar 
# boletos en una taquilla de cine. Lo clientes llegan, se forman al final de la fila y se van
# atendiendo uno por uno en el orden que llegaron.
# Instrucciones: 
# 1. Cree una cola vacía, puede representarse con una lista
# 2. El programa debe mostrar un menú con las siguientes opciones: A) Llegada del cliente
# B) Vender boletos. c) mOSTRAR fILA actual D) Salir
# 3. Cada vez que llegue un cliente, el programa pedira su nombre, y lo agregara al final de
# la cola
# 4. Al vender un boleto, se debe retirar al final de la cola y mostrar un mensaje 
# (cliente tal, a comprado un boleto)
# 5. Si la cola esta vacia y se intenta atender, el programa mostrará 
# "No hay clientes en la fila"
# 6. La cola actual debe mostrarse en cada interaccion o cuando el usuario lo solicite.

cola = []

def mostrar_fila():
    if cola:
        print("\nFila actual:")
        for i, cliente in enumerate(cola, start=1):
            print(f"{i}. {cliente}")
    else:
        print("La fila está vacía.")

while True:
    opcion = input(
        "¿Qué te gustaría hacer?\n"
        "A) Llegada del cliente\n"
        "B) Vender boletos\n"
        "C) Mostrar fila actual\n"
        "D) Salir\n\n"
        "Elige la opción que quieras hacer: "
    ).lower()

    if opcion == "a":
        nombre = input("Ingrese el nombre del cliente: ")
        cola.append(nombre)
        print(f"{nombre} ha llegado y se ha unido a la fila.")
        mostrar_fila()

    elif opcion == "b":
        if cola:
            cliente = cola.pop(0)
            print(f"{cliente} ha comprado un boleto y ha salido de la fila.")
        else:
            print("No hay clientes en la fila.")
        mostrar_fila()

    elif opcion == "c":
        mostrar_fila()

    elif opcion == "d":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor elige A, B, C o D.")
