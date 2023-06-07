#!/usr/bin/env python3
# -*- coding: utf-8 -*-

peso = input("¿Cuál es tu peso en kg?\n")
estatura = input("¿Cuál es tu estatura en metros?\n")
imc = round(float(peso) / float(estatura) ** 2, 2)
print("Tu índice de masa corporal es " + str(imc))
