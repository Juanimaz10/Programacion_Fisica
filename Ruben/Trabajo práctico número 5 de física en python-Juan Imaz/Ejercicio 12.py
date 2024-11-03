import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 12
def problema_12(Ep, masa):
    altura = Ep / (masa * g)
    print(f"Problema 12 - Altura: {altura} m")

problema_12(350, 92)