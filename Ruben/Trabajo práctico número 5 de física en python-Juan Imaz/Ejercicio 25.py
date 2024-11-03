import math

# Constante de aceleración gravitacional
g = 9.8  # m/s^2

# Datos iniciales del problema
masa_25 = 5  # kg
altura_A_B_25 = 0.4  # m (40 cm de altura entre A y B)
velocidad_deseada_B_25 = 1  # m/s, velocidad deseada en B

# a) Calcular la velocidad máxima al pasar por el punto "B"
# Conservación de la energía entre el punto A (potencial) y el punto B (cinética)
energia_potencial_A_25 = masa_25 * g * altura_A_B_25
velocidad_maxima_B_25 = math.sqrt(2 * g * altura_A_B_25)
print(f"Velocidad máxima al pasar por el punto B: {velocidad_maxima_B_25} m/s")

# b) Calcular la altura inicial necesaria para que pase por B con 1 m/s
# Usamos la conservación de energía para encontrar la altura inicial
altura_necesaria_25 = (velocidad_deseada_B_25 ** 2) / (2 * g)
print(f"Altura necesaria para pasar por B con velocidad de 1 m/s: {altura_necesaria_25} m")
