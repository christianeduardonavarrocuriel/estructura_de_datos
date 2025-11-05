# En una oficina hay una impresora compartida, los empleados envian sus 
# documentos para imprimir y los trabajos se van formando en una cola de impresion.
# El programa debe permitir: 
# 1) enviar un nuevo documento a la cola
# 2) imprimir (eliminar) el primer documento en la cola
# 3) mostrar los documentos en espera
# 4) salir del programa
# Condicion: en una cola de impresion para una oficina y por la carga en la misma se 
# debe poder etiquetar un mandato de impresion 
# con tres categorias: urgente, normal, postergado. Las anteriores condiciones deberan
# ser tomadas en la cola y formar las peticiones
# de impresion considerando las etiquetas

print("Bienvenido a la impresora compartida, envie sus documentos\n")

opcion = int(input("¿Qué quieres hacer?\n"
                   "1) Enviar un documento a la cola\n"
                   "2) Imprimir el primer documento en la cola\n"
                   "3) Eliminar el primer documento en la cola\n"
                   "4) Mostrar los documentos en oferta\n"
                   "5) Salir del Programa\n"))

if opcion ==