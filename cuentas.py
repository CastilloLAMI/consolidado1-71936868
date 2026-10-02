class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self._saldo += monto

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= monto

    def consultar_saldo(self) -> float:
        return self._saldo

    def __str__(self) -> str:
        return f"Cuenta N°: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/ {self._saldo:.2f}"

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def calcular_interes(self) -> float:
        return self._saldo * (self.tasa_interes / 100)

    def __str__(self) -> str:
        interes = self.calcular_interes()
        return f"{super().__str__()} | Tasa Interés: {self.tasa_interes}% | Interés Anual: S/ {interes:.2f}"