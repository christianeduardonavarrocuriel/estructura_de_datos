numMaterias = int(input("Escribe el número de materias: "))
numAlumnos = int(input("Escribe el número de alumnos: "))

totalGeneral = 0  # acumulador de todas las calificaciones
alumnos = {}  # diccionario para guardarnombre

for i in range(numAlumnos):
    print(f"\nAlumno {i+1}")
    nombreAlumno = input("Escribe el nombre del alumno: ")
    calificaciones = []

    for j in range(numMaterias):
        calAlumno = int(input(f"Escribe la calificación {j+1} de {nombreAlumno}: "))
        calificaciones.append(calAlumno)

    alumnos[nombreAlumno] = calificaciones  # se guardan las calificaciones

    sumaCalificaciones = sum(calificaciones)
    promedioAlumno = sumaCalificaciones / numMaterias
    print(f"Promedio de calificaciones de {nombreAlumno}: {promedioAlumno}\n")

    totalGeneral += sumaCalificaciones  # sumamos todas las calificaciones

# aquí dividimos por el TOTAL de calificaciones
promedioGeneral = totalGeneral / (numAlumnos * numMaterias)

print(f"\nSuma total de calificaciones de todos los alumnos: {totalGeneral}")
print(f"Promedio general de calificaciones de todos los alumnos: {promedioGeneral}\n")

numBuscar = int(input("Escribe la calificación que quieres buscar: "))

contador = 0
for calificaciones in alumnos.values():
    contador += calificaciones.count(numBuscar)

if contador > 0:
    print(f"\nLa calificación {numBuscar} aparece {contador} veces en total.")
else:
    print(f"\nLa calificación {numBuscar} no existe en ninguna lista.")