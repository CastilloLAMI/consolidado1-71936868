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


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float = 0.0, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        if tasa_interes < 0:
            raise ValueError(f"La tasa de interés no puede ser negativa. Tasa ingresada: {tasa_interes}")
        self.tasa_interes = float(tasa_interes)

    def calcular_interes(self) -> float:
        """Calcula el interés anual basado en el saldo actual. Fórmula: saldo * tasa / 100"""
        return self.consultar_saldo() * self.tasa_interes / 100.0

    def __str__(self) -> str:
        interes_calculado = self.calcular_interes()
        return (f"{super().__str__()} | Tasa Interés: {self.tasa_interes:.1f}% | "
                f"Interés Anual: ${interes_calculado:.2f}")
