import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 3
def problema_3(masa, altura):
    Ep = masa * g * altura
    print(f"Problema 3 - Energía Potencial: {Ep} J")

problema_3(30, 17)