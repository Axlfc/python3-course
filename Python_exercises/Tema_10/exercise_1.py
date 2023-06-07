#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, StringVar, Radiobutton, Label, Button, W  # sudo apt-get install python3-tk


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


root = Tk()

opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Toyota", variable=opcion, value='Toyota', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Hyundai", variable=opcion, value='Hyundai', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Renault", variable=opcion, value='Renault', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Opel", variable=opcion, value='Opel', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
