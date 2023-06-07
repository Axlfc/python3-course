#!/usr/bin/env python3

class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido.")
        else:
            print("El alumno ha aprobado.")


# Creamos los nuevos objetos y los inicializamos
alumno1 = Alumno()
alumno1.inicializar("Mónica", 8)

alumno2 = Alumno()
alumno2.inicializar("Jose", 4)

# Imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()