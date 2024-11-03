import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 14
def problema_14(masa, velocidad):
    Ec = 0.5 * masa * velocidad ** 2
    print(f"Problema 14 - Energía Cinética: {Ec} J")

problema_14(135, 4.17)