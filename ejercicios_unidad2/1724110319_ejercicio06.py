# Cree un programa que permita al usuario ingresar una linea de texto y que cuente cuantas letras dependiendo la eleccion
# existen en esa linea de texto, el usuario podra elegir cualquier letra del alfabeto ya sea mayuscula o minuscula y el 
# sistema entregara el numero de veces que esa letra aparece esa letra repetida, utilice una pila para el desarrollo

texto = input("Ingrese una línea de texto: ")
letra = input("Ingrese la letra que desea contar: ")

texto = texto.lower()
letra = letra.lower()

pila = list(texto)
contador = 0

for i in range(len(pila)):
    caracter = pila.pop()
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en el texto.")
