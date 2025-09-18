# Diseñe un algoritmo recursivo que permita calcular la suma de todos los elementos de enteros, con esto realizar un arreglo
# El arreglo lo debe de recorrer sin utilizar ciclos y la dimensión del mismo es parte del dato de entrada
# Al inicio se pregunta el tamaño del arreglo y dimensión, con esto se pide después los números dentro del arreglo
# Despues de ello tiene que salir la suma de número enteros.

fila = int(input("Escribe el tamaño de tu fila: "))
columna = int(input("Escribe el tamaño de tu columna: "))

if columna == 0 or fila == 0:
    print("Error, no se permite el 0")
else:
    print(f"Tu dimensión es de: {fila} x {columna}")

    # Crear matriz y llenarla
    matriz = []
    for i in range(fila):
        fila_actual = []
        for j in range(columna):
            valor = int(input(f"Escribe el valor en la coordenada ({i},{j}): "))
            fila_actual.append(valor)
        matriz.append(fila_actual)

    # Sumar por fila (primer índice)
    print("\nSuma por filas:")
    for i in range(fila):
        suma = sum(matriz[i])
        print(f"Suma de fila {i}: {suma}")
