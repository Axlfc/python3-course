#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def obtener_impares(lista): 
    resultado = list(filter(lambda x: x % 2 != 0, lista))
    print(resultado)
    resultado = reduce(lambda x, y: x + y, resultado)
    print(resultado)


lista = list(range(100))

obtener_impares(lista)
