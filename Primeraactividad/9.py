def generar_matriz(filas, columnas):
    matriz = []
    contador = 1
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
    
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
filas = 3
columnas = 4
matriz = generar_matriz(filas, columnas)
print("La matriz generada es:")
imprimir_matriz(matriz)
