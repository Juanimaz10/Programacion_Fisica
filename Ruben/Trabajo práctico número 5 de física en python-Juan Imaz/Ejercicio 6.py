import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 6
def problema_6(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 6 - Energía Mecánica Total: {Em} J")

problema_6(18, 7, 6)
