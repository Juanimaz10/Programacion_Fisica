# Datos del problema
altura_derecha = 0  # m (nivel del acantilado derecho)
altura_izquierda = 4  # m
distancia_horizontal = 5  # m
angulo = 30  # grados
gravedad = 9.8  # m/s^2

import math
# a) Velocidad mínima para alcanzar el objetivo
theta = math.radians(angulo)
v_0_min = math.sqrt((distancia_horizontal * gravedad) / math.sin(2 * theta))

# b) Tiempo de vuelo
t_vuelo = (2 * v_0_min * math.sin(theta)) / gravedad

# Mostrar los resultados
print(f"Velocidad mínima para alcanzar el objetivo: {v_0_min:.2f} m/s")
print(f"Tiempo de vuelo: {t_vuelo:.2f} segundos")
