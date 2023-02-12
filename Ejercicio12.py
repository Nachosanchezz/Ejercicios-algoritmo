class Cuenta:
    def __init__(self, nombre, saldo, descubierto=0):
        self.nombre = nombre
        self.saldo = saldo
        self.descubierto = descubierto
        
    def depositar(self, cantidad):
        self.saldo += cantidad
        
    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.descubierto:
            self.saldo -= cantidad
        else:
            print("No hay suficiente saldo en la cuenta para hacer un retiro.")
