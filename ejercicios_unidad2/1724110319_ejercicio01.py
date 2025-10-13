nombre = []
 
nombre = str(input("Escribe el nombre que deseas poner en Fila y en Pila: "))

if len(nombre) == 1 or len(nombre) == 0:
    print("Lo siento, pero nombres que tengan solo 1 letra o ninguna no es valido")

else:
    print(f"Tu palabra en Fila es:",(nombre))
    palabra_pila = nombre[::-1]
    print(f"Tu palabra en Pila es:",(palabra_pila))