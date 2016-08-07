import os

#abrir archivo
datos = open('datos.txt','r+')

# leer archivo
datos_archivo = datos.readline()

# datos de archivo
print datos_archivo

datos_completos = open('datos.txt','r')

# lee todas las lineas del archivo
for linea in datos_completos.readlines():
	print linea

# crear un archivo
nuevo_archivo = open('nuevos_datos.txt','w')

# escribir archivo
nuevo_archivo.write('Nueva Linea')

# cerrar archivo
nuevo_archivo.close()

#remover archivo

os.remove('remover.txt')






