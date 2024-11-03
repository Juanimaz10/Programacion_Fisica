import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 8
def problema_8(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 8 - Energía Mecánica Total: {Em} J")

problema_8(3, 18, 15)