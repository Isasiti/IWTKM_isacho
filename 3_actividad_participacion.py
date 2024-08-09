import math

#Vehículo
class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

#Punto
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

#Rectángulo
class Rectángulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perímetro(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.punto2.x - self.punto1.x)
        alto = abs(self.punto2.y - self.punto1.y)
        return ancho * alto

    def es_cuadrado(self):
        return abs(self.punto2.x - self.punto1.x) == abs(self.punto2.y - self.punto1.y)

#Círculo
class Círculo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perímetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia = self.centro.calcular_distancia(punto)
        return distancia <= self.radio

#Carta
class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
#CuentaBnacaria
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso de ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("El monto del depósito debe ser positivo.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso de ${cantidad}. Saldo actual: ${self.saldo}")
            else:
                print(f"No se puede retirar ${cantidad}. Saldo insuficiente ,esta limpio mi loco. Saldo actual: ${self.saldo}")
        else:
            print("El monto del retiro debe ser positivo.")

    def aplicar_cuota_manejo(self):
        cuota = self.saldo * 0.02
        if self.saldo >= cuota:
            self.saldo -= cuota
            print(f"Cuota de manejo de 2% aplicada. Saldo descontado: ${cuota}. Saldo actual: ${self.saldo}")
        else:
            print("Saldo insuficiente para aplicar la cuota de manejo.")

    def mostrar_detalles(self):
        print(f"Detalles de la cuenta:\nPropietario: {self.titular}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: ${self.saldo}")

    def mostrar_saldo(self):
        print(f"Saldo actual de la cuenta: ${self.saldo}")
cuenta = CuentaBancaria("CabraM", "3229093584", 1000)
cuenta.mostrar_detalles()
cuenta.depositar(500)  # Deposita 500 en la cuenta
cuenta.retirar(300)    # Retira 300 de la cuenta
cuenta.aplicar_cuota_manejo()  # Aplica la cuota de manejo
cuenta.mostrar_detalles()

