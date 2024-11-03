import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 5
def problema_5(Ep, masa):
    altura = Ep / (masa * g)
    print(f"Problema 5 - Altura: {altura} m")

problema_5(50, 15)
