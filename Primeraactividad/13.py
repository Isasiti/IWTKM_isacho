def calcular_operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Indefinida (división por cero)"

    return suma, resta, multiplicacion, division
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma, resta, multiplicacion, division = calcular_operaciones(num1, num2)
    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} y {num2} es: {division}")
except ValueError:
    print("Por favor, ingrese números válidos.")
