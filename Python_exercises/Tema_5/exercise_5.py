#!/usr/bin/env python3

def es_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"¡El año {year} es bisiesto!")
    else:
        print(f"¡El año {year} NO es bisiesto!")


es_bisiesto(int(input("Introduce un año y veamos si es bisiesto...\n")))
