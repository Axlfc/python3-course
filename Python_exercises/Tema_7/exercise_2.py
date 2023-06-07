import time

# Obtenemos la hora actual del sistema y la guardamos en la variable 'hora'
hora = time.strftime('%H')

# Obtenemos los minutos actuales del sistema y los guardamos en la variable 'minutos'
minutos = time.strftime('%M')

# Comprobamos si la hora es mayor o igual a 19 (7 PM)
if int(hora) >= 19:
    print("Es hora de irse a casa")
else:
    # Calculamos las horas restantes restando 19 a la hora actual
    horas_restantes = 19 - int(hora)

    # Calculamos los minutos restantes restando 59 a los minutos actuales
    minutos_restantes = 59 - int(minutos)

    # Mostramos el tiempo restante para irnos a casa
    print("Quedan {} horas y {} minutos para irnos a casa".format(horas_restantes, minutos_restantes))
