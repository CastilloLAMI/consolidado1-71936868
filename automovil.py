class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float, nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError(f"La velocidad máxima debe ser mayor a 0 km/h. Valor ingresado: {valor}")
        self._velocidad_max = float(valor)

    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError(f"El nivel de combustible debe estar entre 0.0 y 100.0%. Valor ingresado: {valor}")
        self._nivel_combustible = float(valor)

    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError(f"El año de fabricación debe estar entre 1886 y 2026. Valor ingresado: {valor}")
        self._año_fabricacion = int(valor)

    def tiempo_llegada(self, distancia_km: float) -> float:
        """Calcula el tiempo de llegada en horas. Fórmula: distancia / velocidad_max"""
        if distancia_km < 0:
            raise ValueError("La distancia no puede ser negativa.")
        return distancia_km / self._velocidad_max

    def __str__(self) -> str:
        return (f"Automóvil: {self.marca} {self.modelo} ({self._año_fabricacion}) | "
                f"Velocidad Máx: {self._velocidad_max} km/h | "
                f"Combustible: {self._nivel_combustible:.1f}%")


if __name__ == "__main__":
    print("=== CREACIÓN Y DEMOSTRACIÓN DE INSTANCIA ===")
    auto = Automovil(
        marca="Toyota",
        modelo="Corolla",
        velocidad_max=180.0,
        nivel_combustible=75.5,
        año_fabricacion=2022
    )
    print(auto)

    # Demostración del método tiempo_llegada
    distancia = 360.0  # km
    tiempo = auto.tiempo_llegada(distancia)
    print(f"Tiempo estimado para recorrer {distancia} km a {auto.velocidad_max} km/h: {tiempo:.2f} horas")

    # Demostración de modificación mediante setters
    print("\n=== USO DE SETTERS ===")
    auto.nivel_combustible = 50.0
    print(f"Nuevo nivel de combustible: {auto.nivel_combustible}%")

    # Prueba de validación con try/except
    print("\n=== PRUEBA DE VALIDACIÓN CON TRY/EXCEPT ===")
    try:
        print("Intentando asignar un año inválido (1800)...")
        auto.año_fabricacion = 1800
    except ValueError as e:
        print(f"Excepción capturada con éxito: {e}")

    try:
        print("\nIntentando asignar nivel de combustible inválido (150%)...")
        auto.nivel_combustible = 150.0
    except ValueError as e:
        print(f"Excepción capturada con éxito: {e}")
