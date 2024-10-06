import math

# Datos del problema
altura_mesa = 0.75  # m
distancia_horizontal = 1.5  # m
gravedad = 9.8  # m/s^2

# a) Tiempo de caída (caída libre)
tiempo = math.sqrt((2 * altura_mesa) / gravedad)

# b) Velocidad horizontal al abandonar la mesa
velocidad_horizontal = distancia_horizontal / tiempo

# Mostrar los resultados
print(f"Tiempo de caída: {tiempo:.2f} segundos")
print(f"Velocidad de la esfera al abandonar la mesa: {velocidad_horizontal:.2f} m/s")
