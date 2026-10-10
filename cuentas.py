class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = str(numero_cuenta)
        self.titular = str(titular)
        if saldo_inicial < 0:
            raise ValueError(f"El saldo inicial no puede ser negativo. Saldo ingresado: {saldo_inicial}")
        self.__saldo = float(saldo_inicial)

    def depositar(self, monto: float):
        # Hotfix: corrección urgente - validar que el monto de depósito sea positivo
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


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, limite_sobregiro: float = 0.0, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        if limite_sobregiro < 0:
            raise ValueError(f"El límite de sobregiro no puede ser negativo. Límite ingresado: {limite_sobregiro}")
        self.limite_sobregiro = float(limite_sobregiro)

    def retirar(self, monto: float):
        """Sobreescribe retirar permitiendo sobregiro hasta saldo + limite_sobregiro."""
        if monto <= 0:
            raise ValueError(f"El monto a retirar debe ser mayor a 0. Monto ingresado: {monto}")
        saldo_actual = self.consultar_saldo()
        disponible = saldo_actual + self.limite_sobregiro
        if monto > disponible:
            raise ValueError(
                f"Límite de sobregiro excedido. Saldo disponible con sobregiro: ${disponible:.2f}, "
                f"Monto solicitado: ${monto:.2f}"
            )
        self._ajustar_saldo(saldo_actual - float(monto))

    def permite_sobregiro(self) -> bool:
        """Retorna True si el saldo actual es negativo, False si no."""
        return self.consultar_saldo() < 0

    def __str__(self) -> str:
        en_sobregiro = "Sí" if self.permite_sobregiro() else "No"
        return (f"{super().__str__()} | Límite Sobregiro: ${self.limite_sobregiro:.2f} | "
                f"En Sobregiro: {en_sobregiro}")


if __name__ == "__main__":
    print("=== PRUEBA DE CUENTA DE AHORROS ===")
    ahorros = CuentaAhorros(numero_cuenta="AH-1001", titular="Ivan Castillo", tasa_interes=4.5)
    ahorros.depositar(1000.0)
    print(ahorros)

    print("\n--- Operaciones en Cuenta de Ahorros ---")
    ahorros.depositar(500.0)
    print(f"Depósito de $500.00 realizado -> Saldo actual: ${ahorros.consultar_saldo():.2f}")
    ahorros.retirar(200.0)
    print(f"Retiro de $200.00 realizado -> Saldo actual: ${ahorros.consultar_saldo():.2f}")
    interes = ahorros.calcular_interes()
    print(f"Interés generado anual: ${interes:.2f}")
    print(ahorros)

    print("\n=== PRUEBA DE CUENTA CORRIENTE ===")
    corriente = CuentaCorriente(numero_cuenta="CC-2002", titular="Ramiro Mamani", limite_sobregiro=200.0)
    corriente.depositar(300.0)
    print(corriente)

    print("\n--- Operaciones en Cuenta Corriente ---")
    corriente.depositar(100.0)
    print(f"Depósito de $100.00 realizado -> Saldo actual: ${corriente.consultar_saldo():.2f}")
    print("Retirando $550.00 (utilizando sobregiro)...")
    corriente.retirar(550.0)
    print(f"Saldo tras retiro: ${corriente.consultar_saldo():.2f}")
    print(f"¿Está en sobregiro? {corriente.permite_sobregiro()}")
    print(corriente)

    print("\n--- Intento de retiro que supera el límite de sobregiro ---")
    try:
        corriente.retirar(100.0)
    except ValueError as e:
        print(f"Excepción capturada correctamente: {e}")
