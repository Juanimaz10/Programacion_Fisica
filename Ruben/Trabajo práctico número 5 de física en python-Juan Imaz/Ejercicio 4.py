import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Problema 4
def problema_4(Ep, altura):
    masa = Ep / (g * altura)
    print(f"Problema 4 - Masa: {masa} kg")

problema_4(625, 25)