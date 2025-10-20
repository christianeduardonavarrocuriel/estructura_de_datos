# Cree un programa en Python que determine, si una expresión tiene los paréntesis correctamente 
# balanceados para ello utilice una pila que almacene los paréntesis de apertura y lo retire cuando 
# encuentre un paréntesis de cierre 

# Una expresión está balanceada si: 
# Cada paréntesis de apertura tiene su correspondiente cierre. No hay cierres antes de que haya un paréntesis de apertura

# Programa para verificar si los paréntesis están balanceados

# Verificar si los paréntesis están balanceados sin usar variables extra

expresion = input("Escribe una expresión con paréntesis: ")

pila = []

for caracter in expresion:
    if caracter == '(':
        pila.append(caracter)
    elif caracter == ')':
        if not pila:
            print("Los paréntesis NO están balanceados.")
            break
        else:
            pila.pop()
else:
    # Este else se ejecuta solo si el for terminó sin break
    if not pila:
        print("Los paréntesis están correctamente balanceados.")
    else:
        print("Los paréntesis NO están balanceados.")
