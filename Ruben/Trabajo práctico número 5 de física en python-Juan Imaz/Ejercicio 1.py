import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 1
def problema_1(masa, velocidad):
    Ec = 0.5 * masa * velocidad ** 2
    print(f"Problema 1 - Energía Cinética: {Ec} J")

problema_1(72, 15)