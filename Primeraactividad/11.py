def generar_pares():
    pares = [numero for numero in range(1, 101) if numero % 2 == 0]
    return pares
lista_pares = generar_pares()
print(f'Los números pares entre 1 y 100 son: {lista_pares}')
