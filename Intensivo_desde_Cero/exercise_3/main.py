def calcular_numeros_primos(N):
    primos = []

    for num in range(2, N + 1):
        es_primo = True

        # Verificar si el número es divisible por algún número menor
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        # Agregar el número a la lista de primos si es primo
        if es_primo:
            primos.append(num)

    return primos


def main():
    primos = calcular_numeros_primos(20)
    print(primos)


if __name__ == '__main__':
    main()
