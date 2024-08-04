def es_palindromo(cadena):
    cadena_limpia = ''.join(cadena.split()).lower()
    return cadena_limpia == cadena_limpia[::-1]
cadena_usuario = input("Ingrese una cadena de texto: ")
if es_palindromo(cadena_usuario):
    print("es un palíndromo.")
else:
    print("no es un palíndromo.")
