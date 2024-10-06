import math

# Datos del problema
v_0 = 25  # m/s (velocidad inicial)
angulo = 45  # grados
gravedad_luna = 1.6  # m/s^2 (aceleración en la Luna)

# Convertir ángulo a radianes
theta = math.radians(angulo)

# a) Alcance máximo
alcance_maximo = (v_0**2 * math.sin(2 * theta)) / gravedad_luna

# b) Tiempo total de vuelo
tiempo_vuelo = (2 * v_0 * math.sin(theta)) / gravedad_luna

# Mostrar los resultados
print(f"Alcance máximo: {alcance_maximo:.2f} metros")
print(f"Tiempo total de vuelo: {tiempo_vuelo:.2f} segundos")
