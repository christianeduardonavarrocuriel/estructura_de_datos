n = int(input("Escribe un número entero: "))

a = 0
b = 1
 
if n < 1:
    print ("Error: Solo números positivos")
elif n >= 1:
    print (a)
    print (b)

for i in range(2,n):
    z = a + b
    print (z)
    a, b = b, z