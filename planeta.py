import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = float(masa)
        self.radio = float(radio)
        self.distancia_al_sol = float(distancia_al_sol)
        self.tiene_vida = tiene_vida
