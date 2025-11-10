# En una oficina hay una impresora compartida, los empleados envían sus 
# documentos para imprimir y los trabajos se van formando en una cola de impresión.
# El programa debe permitir: 
# 1) Enviar un nuevo documento a la cola
# 2) Imprimir (eliminar) el primer documento en la cola
# 3) Mostrar los documentos en espera
# 4) Salir del programa
# Condición: en una cola de impresión para una oficina y por la carga en la misma 
# se debe poder etiquetar un mandato de impresión con tres categorías: 
# urgente, normal, postergado. 
# Las anteriores condiciones deberán ser tomadas en la cola y formar las peticiones
# de impresión considerando las etiquetas.

print("Bienvenido a la impresora compartida\n")

cola_urgente = []
cola_normal = []
cola_postergado = []

contador = 1

while True:
    opcion = int(input("¿Qué desea hacer?\n"
                       "1) Enviar un nuevo documento a la cola\n"
                       "2) Imprimir el primer documento en la cola\n"
                       "3) Mostrar los documentos en espera\n"
                       "4) Salir del programa\n"
                       "Seleccione una opción: "))

    if opcion == 1:
        prioridad = input("Ingrese la prioridad a través de incisos:\n"
                          "A) Urgente\n"
                          "B) Normal\n"
                          "C) Postergado\n"
                          "Seleccione una opción: ").upper()

        documento = f"Documento {contador}"
        contador += 1

        if prioridad == "A":
            cola_urgente.append(documento)
            print("Se ha agregado un documento URGENTE a la cola.")
        elif prioridad == "B":
            cola_normal.append(documento)
            print("Se ha agregado un documento NORMAL a la cola.")
        elif prioridad == "C":
            cola_postergado.append(documento)
            print("Se ha agregado un documento POSTERGADO a la cola.")
        else:
            print("Opción no válida. Intente nuevamente.")

    elif opcion == 2:
        if cola_urgente:
            print("Imprimiendo documento URGENTE:", cola_urgente.pop(0))
        elif cola_normal:
            print("Imprimiendo documento NORMAL:", cola_normal.pop(0))
        elif cola_postergado:
            print("Imprimiendo documento POSTERGADO:", cola_postergado.pop(0))
        else:
            print("No hay documentos en la cola para imprimir.")

    elif opcion == 3:
        print("\nDocumentos en espera:")
        # 🔹 Simplificación de la condición:
        if not (cola_urgente or cola_normal or cola_postergado):
            print("No hay documentos en espera.")
        else:
            print("Urgentes:", cola_urgente)
            print("Normales:", cola_normal)
            print("Postergados:", cola_postergado)

    elif opcion == 4:
        print("Adiós :)")
        break

    else:
        print("Inténtelo de nuevo, esta opción no existe en el sistema")

    print("\nEstado actual de la cola:")
    print("Urgentes:", cola_urgente)
    print("Normales:", cola_normal)
    print("Postergados:", cola_postergado)