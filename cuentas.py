class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = str(numero_cuenta)
        self.titular = str(titular)
        if saldo_inicial < 0:
            raise ValueError(f"El saldo inicial no puede ser negativo. Saldo ingresado: {saldo_inicial}")
        self.__saldo = float(saldo_inicial)

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError(f"El monto a depositar debe ser mayor a 0. Monto ingresado: {monto}")
        self.__saldo += float(monto)

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError(f"El monto a retirar debe ser mayor a 0. Monto ingresado: {monto}")
        if monto > self.__saldo:
            raise ValueError(f"Saldo insuficiente. Saldo disponible: ${self.__saldo:.2f}, Monto solicitado: ${monto:.2f}")
        self.__saldo -= float(monto)

    def consultar_saldo(self) -> float:
        return self.__saldo

    def _ajustar_saldo(self, nuevo_saldo: float):
        """Método protegido para actualizar saldo en operaciones de sobregiro de subclases."""
        self.__saldo = float(nuevo_saldo)

    def __str__(self) -> str:
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: ${self.__saldo:.2f}"
