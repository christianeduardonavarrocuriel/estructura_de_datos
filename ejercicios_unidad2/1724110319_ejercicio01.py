nombre = input("Escribe una palabra: ")

if len(nombre) <= 1:
    print("Lo siento, las palabras con 1 letra o ninguna no se pueden invertir")
else:
    pila = list(nombre)

    print("Tu palabra en Fila es:", nombre)

    print("Tu palabra en Pila es: " , end = "")
    while pila:
        print(pila.pop(), end = "")
    print()