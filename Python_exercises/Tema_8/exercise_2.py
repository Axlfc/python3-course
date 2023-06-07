#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pickle import dump, load

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas

toyota = Vehiculo("Rojo", "4")
print(toyota)

# Guardar el objeto en un archivo
with open('vehiculo_objeto', 'w+b') as file:
    dump(toyota, file)

# Cargar el objeto desde el archivo
with open('vehiculo_objeto', 'rb') as file:
    nuevo_toyota = load(file)

print(nuevo_toyota)
