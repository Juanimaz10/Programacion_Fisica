import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 10
def problema_10(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 10 - Energía Mecánica Total: {Em} J")

problema_10(8, 5, 8)