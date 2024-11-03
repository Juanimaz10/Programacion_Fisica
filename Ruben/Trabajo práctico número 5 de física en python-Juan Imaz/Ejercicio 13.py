import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 13
def problema_13(Ep, masa):
    altura = Ep / (masa * g)
    print(f"Problema 13 - Altura: {altura} m")

problema_13(280, 115)