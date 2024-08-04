def calcular_media(lista_numeros):
    if not lista_numeros:
        return "La lista está vacía"
    
    suma = sum(lista_numeros)
    media = suma / len(lista_numeros)
    return media
numeros = [10, 22, 33, 44, 501]
media = calcular_media(numeros)
print(f'La media aritmética de la lista es: {media}')
