#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Creación del archivo y escritura en él
file = open('mi_primer_archivo.txt', 'w')
file.write('¡He creado mi primer archivo!\n')
file.close()

# Apertura del archivo, lectura y escritura adicional
file = open('mi_primer_archivo.txt', 'r+')
file.readline()  # Leer una línea sin almacenarla en una variable
file.write('Esta es la segunda vez que escribo.\n')

# Regresar al inicio del archivo y leer todo el contenido
file.seek(0)
contenido = file.read()

# Imprimir el contenido del archivo
print(contenido)

# Cerrar el archivo
file.close()
