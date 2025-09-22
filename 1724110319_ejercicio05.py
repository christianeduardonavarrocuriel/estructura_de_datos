# Busqueda de diseño en un arreglo: Diseña un programa en python que permita declarar y crear un arreglo con calificaciones de
# un grupo de estudiantes (valores enteros del 0 al 100). 2. Calcule el promedio de las calificaciones de cada alumno
# y de las calificaciones almacenadas en el arreglo. 3. Que permita buscar si una calificación especifica 
# (ingresada por el usuario) se encuentra en el arreglo. 4. Que muestre los resultados de forma clara en la pantalla.

numMaterias = int(input("Escribe el número de materias: "))
numAlumnos = int(input("Escribe el número de alumnos: "))

for i in range(numAlumnos):
    nombreAlumno = input("Escribe el nombre del alumno: ")
    print(f"Alumno: {nombreAlumno}")

    for j in range(numMaterias):
        calAlumno = int(input(f"Escribe la calificación {j+1} de {nombreAlumno}: "))

