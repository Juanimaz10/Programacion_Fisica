import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 2
def problema_2(Ec, masa):
    velocidad = math.sqrt((2 * Ec) / masa)
    print(f"Problema 2 - Velocidad: {velocidad} m/s")

problema_2(530, 58)