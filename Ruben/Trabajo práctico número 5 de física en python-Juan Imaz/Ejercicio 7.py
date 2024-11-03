import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 7
def problema_7(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 7 - Energía Mecánica Total: {Em} J")

problema_7(8, 7, 9)
