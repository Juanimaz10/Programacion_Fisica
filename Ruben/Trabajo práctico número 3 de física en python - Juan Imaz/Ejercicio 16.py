import math
# Datos del problema
v_0 = 40  # m/s (velocidad inicial)
altura_torre = 50  # m
gravedad = 9.8  # m/s^2

# a) Velocidad en la altura máxima (es 0)
velocidad_max = 0

# b) Altura máxima alcanzada
altura_maxima = altura_torre + (v_0**2) / (2 * gravedad)

# c) Tiempo total (suma del tiempo de subida y tiempo de caída)
tiempo_subida = v_0 / gravedad
tiempo_caida = math.sqrt(2 * altura_maxima / gravedad)
tiempo_total = tiempo_subida + tiempo_caida

# Mostrar los resultados
print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
print(f"Tiempo total de vuelo: {tiempo_total:.2f} segundos")
