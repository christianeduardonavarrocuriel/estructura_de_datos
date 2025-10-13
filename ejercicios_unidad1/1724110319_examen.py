# Implementa en python un programa que realice lo siguiente:
# 1. Cree un arreglo con las calificaciones de los 10 estudiantes considerando los valores enteros de entre 0 y 10.
# 2. Al inicio se preguntará cuantas materias están en el curso
# 3. Muestra en pantalla a los alumnos y todas las calificaciones
# 4. Calcule y muestres promedio de las calificaciones por alumno y grupal
# 5. Promedio de las calificaciones por materia
# 6. La calificación minima y la calficación maxima
# 7. El número de estudiantes que aprobaron (igual a 7) y los que reprobaron (menor a 7)
# 8. Permita al usuario buscar una calificación especifica dentro del arreglo e indique si se encuentra o no 
# 9. Después de la busqueda ordene el arreglo de mayor a menor y muestre el resultado en pantalla

numAlumnos = 10 

nombres = []
calificaciones = []

print("Escribe el nombre de los alumnos (Max 10): ")

for i in range(numAlumnos):
    nombre = input(f"Escribe el nombre del alumno {i+1}: ")
    nombres.append(nombre)
    calificaciones.append([])

numMaterias = int(input("¿Cuántas materias serán? "))

for i in range(numAlumnos):
    print(f"\nIngresa las calificaciones de {nombres[i]}:")
    for j in range(numMaterias):
        cal = int(input(f"Calificación de la materia {j+1} (0 a 10): "))
        calificaciones[i].append(cal)

print("\nCalificaciones de los alumnos")
for i in range(numAlumnos):
    print(f"{nombres[i]}: {calificaciones[i]}")

print("\nPromedio de cada alumno")
for i in range(numAlumnos):
    sumaCalificaciones = sum(calificaciones[i])
    promedioAlumno = sumaCalificaciones / numMaterias
    print(f"{nombres[i]}: {promedioAlumno}")

totalGeneral = 0
for i in range(numAlumnos):
    totalGeneral += sum(calificaciones[i])

promedioGeneral = totalGeneral / (numAlumnos * numMaterias)
print(f"\nPromedio general del grupo: {promedioGeneral}")

# Promedio por materia
print("\nPromedio por materia")
for j in range(numMaterias):
    sumaMateria = 0
    for i in range(numAlumnos):
        sumaMateria += calificaciones[i][j]
    promedioMateria = sumaMateria / numAlumnos
    print(f"Materia {j+1}: {promedioMateria}")

minima = 10
maxima = 0
for i in range(numAlumnos):
    for cal in calificaciones[i]:
        if cal < minima:
            minima = cal
        if cal > maxima:
            maxima = cal

print("\nCalificación mínima y máxima")
print(f"Calificación máxima: {maxima}")
print(f"Calificación mínima: {minima}")

aprobados = 0
reprobados = 0
for i in range(numAlumnos):
    aprobado = True
    for cal in calificaciones[i]:
        if cal < 7:
            aprobado = False
            break
    if aprobado:
        aprobados += 1
    else:
        reprobados += 1

print("\nAprobados y reprobados por materia")
for j in range(numMaterias):
    aprobados_materia = 0
    reprobados_materia = 0
    for i in range(numAlumnos):
        if calificaciones[i][j] >= 7:
            aprobados_materia += 1
        else:
            reprobados_materia += 1
    print(f"Materia {j+1}: Aprobados {aprobados_materia}, Reprobados {reprobados_materia}")

buscar = int(input("\nIngrese la calificación a buscar: "))

encontrado = False
for i in range(numAlumnos):
    for cal in calificaciones[i]:
        if cal == buscar:
            encontrado = True
            break
    if encontrado:
        break

if encontrado:
    print(f"La calificación {buscar} sí se encuentra")
else:
    print(f"La calificación {buscar} no se encuentra")

todasCalificaciones = []
for i in range(numAlumnos):
    for cal in calificaciones[i]:
        todasCalificaciones.append(cal)

todasCalificaciones.sort(reverse=True)

print("\nCalificaciones ordenadas de mayor a menor")
print(todasCalificaciones)