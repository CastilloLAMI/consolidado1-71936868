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

    def __str__(self) -> str:
        tipo = "Exterior" if self.es_planeta_exterior() else "Interior"
        densidad = self.calcular_densidad()
        vida = "SÃ­" if self.tiene_vida else "No"
        return (f"Planeta: {self.nombre} | Tipo: {tipo} | "
                f"Densidad: {densidad:.2f} kg/mÂ³ | "
                f"Distancia al Sol: {self.distancia_al_sol} UA | Tiene vida: {vida}")

if __name__ == "__main__":
    tierra = Planeta(
        nombre="Tierra",
        masa=5.972e24,
        radio=6.371e6,
        distancia_al_sol=1.0,
        tiene_vida=True
    )

    jupiter = Planeta(
        nombre="JÃºpiter",
        masa=1.898e27,
        radio=6.9911e7,
        distancia_al_sol=5.204,
        tiene_vida=False
    )

    marte = Planeta(
        nombre="Marte",
        masa=6.417e23,
        radio=3.3895e6,
        distancia_al_sol=1.524,
        tiene_vida=False
    )

    print("=== INFORMACIÃ“N DE PLANETAS ===")
    print(tierra)
    print(jupiter)
    print(marte)
