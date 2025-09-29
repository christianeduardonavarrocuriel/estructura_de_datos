#Diseñe un programa. Declare y cree un arreglo con edades de un grupo de personas
#Calcule e imprima la edad minima y la edad maxima del grupo de personas con el nombre de estas, el promedio de las edades y
#y la mediana del grupo. Permita al usuario agregar una nueva edad al arreglo y mostrar nuevamente los datos actualizados

personas = int(input("Escribe el número de personas que quieres que existan: "))

totalPersonas = 0
edad = 0

for i in range(personas):
    nombrePersonas= input(f"Escribe el nombre de la persona {i+1}: ")
    nombre = []

for j in range(personas):
    edad = int(input(f"Escribe la edad de la persona número {j+1}: "))
    nombre.append(edad)


