class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float, nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max            
        self.nivel_combustible = nivel_combustible    
        self.año_fabricacion = año_fabricacion        

    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError("El año de fabricación debe estar entre 1886 y 2026.")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0%.")
        self._nivel_combustible = float(valor)

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser mayor a 0 km/h.")
        self._velocidad_max = float(valor)

    def tiempo_llegada(self, distancia_km: float) -> float:
        return distancia_km / self.velocidad_max

    def __str__(self) -> str:
        return f"Auto: {self.marca} {self.modelo} ({self.año_fabricacion}) | Vel. Máx: {self.velocidad_max} km/h | Combustible: {self.nivel_combustible}%"

if __name__ == "__main__":
    auto1 = Automovil("Toyota", "Corolla", 180.0, 75.0, 2020)
    print(auto1)
    print(f"Tiempo para recorrer 360 km: {auto1.tiempo_llegada(360):.2f} horas")

    try:
        auto1.año_fabricacion = 1800
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")