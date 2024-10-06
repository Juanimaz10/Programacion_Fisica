import math

# Datos del problema
altura = 2000  # m
velocidad_bombardero_kmh = 800  # km/h
distancia_objetivo = 5000  # m
gravedad = 9.8  # m/s^2

# Convertir velocidad a m/s
velocidad_bombardero = velocidad_bombardero_kmh * 1000 / 3600

# a) Tiempo en el aire (caída libre)
tiempo_caida = math.sqrt((2 * altura) / gravedad)

# b) Distancia horizontal recorrida por la bomba
distancia_caida = velocidad_bombardero * tiempo_caida

# c) Posición del bombardero al explotar la bomba
distancia_bombardero_al_explotar = velocidad_bombardero * tiempo_caida

# Mostrar los resultados
print(f"Tiempo de caída: {tiempo_caida:.2f} segundos")
print(f"Distancia horizontal recorrida por la bomba: {distancia_caida:.2f} metros")
print(f"Posición del bombardero al explotar la bomba: {distancia_bombardero_al_explotar:.2f} metros")
