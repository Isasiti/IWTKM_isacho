def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
numero = 3
print(f'El factorial de {numero} es: {factorial(numero)}')
