import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 9
def problema_9(masa, altura, velocidad):
    Ep = masa * g * altura
    Ec = 0.5 * masa * velocidad ** 2
    Em = Ep + Ec
    print(f"Problema 9 - Energía Mecánica Total: {Em} J")

problema_9(5, 10, 9)

