import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 15
def problema_15(Ec, masa):
    velocidad = math.sqrt((2 * Ec) / masa)
    print(f"Problema 15 - Velocidad: {velocidad} m/s")

problema_15(92, 45)