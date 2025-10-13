#Diseñe un programa. Declare y cree un arreglo con edades de un grupo de personas
#Calcule e imprima la edad minima y la edad maxima del grupo de personas con el nombre de estas, el promedio de las edades y
#y la mediana del grupo. Permita al usuario agregar una nueva edad al arreglo y mostrar nuevamente los datos actualizados

# Pedimos cuántas personas hay
personas = int(input("¿Cuántas personas hay?: "))

# Listas para guardar datos
nombres = []
edades = []

# Captura de datos
for i in range(personas):
    nombre = input(f"Nombre de la persona {i+1}: ")
    edad = int(input(f"Edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)

# ---- Cálculos iniciales ----
# Edad mínima
edad_min = min(edades)
nombre_min = nombres[edades.index(edad_min)]

# Edad máxima
edad_max = max(edades)
nombre_max = nombres[edades.index(edad_max)]

# Promedio (media)
media = sum(edades) / len(edades)

# Mediana
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    mediana = (edades_ordenadas[n//2 - 1] + edades_ordenadas[n//2]) / 2
else:
    mediana = edades_ordenadas[n//2]

# Mostrar resultados en orden
print("\n--- Resultados iniciales ---")
print("1) Edad mínima:", edad_min, "Nombre:", nombre_min)
print("2) Edad máxima:", edad_max, "Nombre:", nombre_max)
print("3) Promedio (media):", media)
print("4) Mediana:", mediana)

# ---- Agregar nueva persona ----
nuevo_nombre = input("\nNombre de la nueva persona: ")
nueva_edad = int(input("Edad de la nueva persona: "))
nombres.append(nuevo_nombre)
edades.append(nueva_edad)

# Recalcular
edad_min = min(edades)
nombre_min = nombres[edades.index(edad_min)]
edad_max = max(edades)
nombre_max = nombres[edades.index(edad_max)]
media = sum(edades) / len(edades)
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    mediana = (edades_ordenadas[n//2 - 1] + edades_ordenadas[n//2]) / 2
else:
    mediana = edades_ordenadas[n//2]

# Mostrar resultados actualizados en el mismo orden
print("\n--- Resultados con nueva persona ---")
print("1) Edad mínima:", edad_min, "Nombre:", nombre_min)
print("2) Edad máxima:", edad_max, "Nombre:", nombre_max)
print("3) Promedio (media):", media)
print("4) Mediana:", mediana)

