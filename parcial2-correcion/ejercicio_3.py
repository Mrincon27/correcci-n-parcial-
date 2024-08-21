def diferencia_listas(x, y):
    return list(set(x) - set(y))

def diferencia():
    x = [1, 2, 3, 4, 5]  # Definir x y y dentro de la función diferencia
    y = [4, 5, 6, 7, 8]
    resultado = diferencia_listas(x, y)
    print("Elementos en la primera lista que no están en la segunda lista:", resultado)

