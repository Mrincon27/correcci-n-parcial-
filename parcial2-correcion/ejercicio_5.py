def calcular_mediana():
    arreglo = [12, 4, 5, 3, 8, 7]
    x_ordenado = sorted(arreglo)
    n = len(x_ordenado)
    if n % 2 == 0:
        mediana = (x_ordenado[n//2 - 1] + x_ordenado[n//2]) / 2
    else:
        mediana = x_ordenado[n//2]
    print(f"la mediana de los numeros es 12, 4, 5, 3, 8, 7 es: {mediana}")




