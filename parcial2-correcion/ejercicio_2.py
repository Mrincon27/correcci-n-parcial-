def contienevocal(x):
    vocales = 'a','e','i','o','u','A','E','I','O','U'
    cadena=input("ingrese una cadena de caracteres:")
    contador=0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    if contador >= 2:
        print("La cadena contiene dos o más vocales.")
    else:
        print("La cadena no contiene dos o más vocales.")