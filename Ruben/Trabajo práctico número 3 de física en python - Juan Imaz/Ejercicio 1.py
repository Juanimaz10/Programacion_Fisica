import math

# Datos del problema
altura = 1920  # m
velocidad_horizontal = 90  # m/s
gravedad = 9.8  # m/s^2

# a) Tiempo en el aire (caída libre)
tiempo = math.sqrt((2 * altura) / gravedad)

# b) Distancia recorrida horizontalmente
distancia_horizontal = velocidad_horizontal * tiempo

# c) Componentes de la velocidad al llegar al suelo
velocidad_vertical = gravedad * tiempo
velocidad_total = math.sqrt(velocidad_horizontal**2 + velocidad_vertical**2)

# Mostrar los resultados
print(f"Tiempo de caída: {tiempo:.2f} segundos")
print(f"Distancia horizontal recorrida: {distancia_horizontal:.2f} metros")
print(f"Velocidad horizontal al impactar: {velocidad_horizontal:.2f} m/s")
print(f"Velocidad vertical al impactar: {velocidad_vertical:.2f} m/s")
print(f"Velocidad total al impactar: {velocidad_total:.2f} m/s")
