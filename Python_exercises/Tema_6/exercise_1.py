#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color: {}, {} ruedas, {} puertas".format(self.color, self.ruedas, self.puertas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color: {}, Velocidad: {} km/h, {} ruedas, {} puertas, Cilindrada: {} cc".format(
            self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada
        )


# Crear un objeto de la clase Coche
my_car = Coche("Rojo", 4, 2, 190, 1400)

# Mostrar el objeto por consola utilizando el método __str__()
print(my_car)
