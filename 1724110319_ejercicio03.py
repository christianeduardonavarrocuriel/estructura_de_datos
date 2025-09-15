# Desarrolle un algoritmo recursivo que recibe una cadena de texto y devuelva la misma cadena invertida, si la cadena esta vacia 
# o tiene un solo caracter devolver de la misma manera

p = str(input("Escribe una palabra que deseas invertir: " ))

if len(p) == 1 or len(p) == 0:
    print("Tu Texto es vacío o muy corto, solo se imrpimira el mismo caracter: ")
    print(p)
    
else:
    palabra_invertida = p[::-1] 
    print("Tu palabra al revés es: ")
    print((palabra_invertida))
    
    
## La función [::-1] nos ayudará a invertir texto