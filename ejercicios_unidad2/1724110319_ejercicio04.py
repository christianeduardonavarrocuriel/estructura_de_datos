# Revertir una cadena de palabras utilizando una pila. 
# Descripcion: cree un programa que permita al usuario ingresar una linea de texto y 
# que utilizando una pila muestre la pila de texto invertida. 
# La linea de texto no tendra maximo de palabras sino que al darle enter mostrará el resultado

palabra = input("Escribe la cadena de palabras que deseas invertir: ")

if len(palabra) <= 1:
    print("Error")
else:
    pila = list(palabra)

    print("Tu cadena de palabras invertida se ve asi: ", end = "")
    while pila:
        print(pila.pop(), end = "")
    print()