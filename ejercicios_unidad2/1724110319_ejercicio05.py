# desarrollar un programa que evalúe una línea de texto 
# y cuente, el número de caracteres especiales que se escriben en la línea.
# la línea de texto no tiene límite y al finalizar el último valor entregado será el número de caracteres especiales 
# incluyendo el espacio. Utilice una pila para el desarrollo

palabra = input("Escribe la palabra que deseas saber cuantos caracteres especiales tiene: ")

caracteres_especiales = set(r'''  #$%&'()*+,°|Ññ!¡"-./:;<=>?@[\]^_`¨{|}~1234567890´ ''')

pila = list(palabra)

contador = 0

invertida = ""
while pila:
    caracter = pila.pop()
    if caracter in caracteres_especiales or caracter == " ":
        contador += 1

print(f"La cantidad de caracteres especiales son (incluyendo espacios):",(contador))