import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 11
def problema_11(Ep, altura):
    masa = Ep / (g * altura)
    print(f"Problema 11 - Masa: {masa} kg")

problema_11(780, 9)