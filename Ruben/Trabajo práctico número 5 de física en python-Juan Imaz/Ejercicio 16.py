import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 16
def problema_16(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 16 - Energía Mecánica Total: {Em} J")

problema_16(750, 120, 58)