# En una cafetería se atienden a los clientes que llegan a ordenar diferentes tipos de café.
# Los clientes pueden ordenar diversos tipos de café, pero existe una promoción especial: 
# aquellos clientes que soliciten el "café del día" (Americano) serán atendidos con prioridad.
# El programa debe permitir:
# 1) Agregar un cliente a la cola con su pedido
# 2) Atender al siguiente cliente (prioridad a quienes ordenaron café del día)
# 3) Mostrar la cola de espera
# 4) Salir del sistema
# Condición: Los clientes que ordenan el café del día (Americano) tienen prioridad 
# y serán atendidos primero antes que los demás clientes.

print("Bienvenido a la Cafetería\n")

cola_cafe_del_dia = []  # Cola para clientes que ordenaron café del día (Americano)
cola_normal = []  # Cola para clientes con otros pedidos

contador = 1

while True:
    opcion = int(input("¿Qué desea hacer?\n"
                       "1) Agregar un cliente a la cola\n"
                       "2) Atender al siguiente cliente\n"
                       "3) Mostrar la cola de espera\n"
                       "4) Salir del sistema\n"
                       "Seleccione una opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del cliente: ")
        tipo_cafe = input("¿Qué tipo de café desea ordenar?\n"
                         "A) Café del día (Americano)\n"
                         "B) Otro tipo de café\n"
                         "Seleccione una opción: ").upper()

        cliente = f"Cliente {contador}: {nombre}"
        contador += 1

        if tipo_cafe == "A":
            cola_cafe_del_dia.append(cliente)
            print(f"Se ha agregado {nombre} a la cola (CAFÉ DEL DÍA - Americano).")
        elif tipo_cafe == "B":
            cola_normal.append(cliente)
            print(f"Se ha agregado {nombre} a la cola (Pedido normal).")
        else:
            print("Opción no válida. Intente nuevamente.")

    elif opcion == 2:
        if cola_cafe_del_dia:
            print("Atendiendo cliente con CAFÉ DEL DÍA:", cola_cafe_del_dia.pop(0))
        elif cola_normal:
            print("Atendiendo cliente con pedido normal:", cola_normal.pop(0))
        else:
            print("No hay clientes en la cola para atender.")

    elif opcion == 3:
        print("\nClientes en espera:")
        if not (cola_cafe_del_dia or cola_normal):
            print("No hay clientes en espera.")
        else:
            print("Café del día (Americano):", cola_cafe_del_dia)
            print("Pedidos normales:", cola_normal)

    elif opcion == 4:
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor intente nuevamente.")

    print("\nEstado actual de la cola:")
    print("Café del día (Americano):", cola_cafe_del_dia)
    print("Pedidos normales:", cola_normal)
