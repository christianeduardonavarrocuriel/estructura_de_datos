# Verificar utilizando pilas si una palabra es un palindromo o no lo es:
# 1. Solicitar al usuario la palabra
# 2. Utilizar la pila para invertir la palabra
# 3. Comparar
# unal vs invertida (si son iguales = palindromo y si son diferentes debe decir que no es palindromo)

palabra = input("Escribe la palabra que quieres saber si al invertir es palíndromo: ")

palabra = palabra.lower().replace(" ", "")

pila = list(palabra)

invertida = ""
while pila:
    invertida += pila.pop()

if palabra == invertida:
    print(f"Escribiste {palabra}, es un palíndromo.")
else:
    print(f"Escribiste {palabra}, no es un palíndromo.")