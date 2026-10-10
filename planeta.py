import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = float(masa)
        self.radio = float(radio)
        self.distancia_al_sol = float(distancia_al_sol)
        self.tiene_vida = tiene_vida

    def calcular_densidad(self) -> float:
        """Calcula la densidad media en kg/mÂ³. Formula: masa / ((4/3) * pi * radio^3)"""
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        """Retorna True si la distancia media al Sol es mayor a 5.2 UA, False en caso contrario."""
        return self.distancia_al_sol > 5.2
