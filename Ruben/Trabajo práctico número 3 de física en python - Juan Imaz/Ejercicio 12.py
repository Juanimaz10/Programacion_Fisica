import math

# Datos del problema
altura = 2000  # m
velocidad_avion_kmh = 900  # km/h
velocidad_barco_kmh = 40  # km/h
gravedad = 9.8  # m/s^2

# Convertir velocidades a m/s
velocidad_avion = velocidad_avion_kmh * 1000 / 3600
velocidad_barco = velocidad_barco_kmh * 1000 / 3600

# a) Tiempo de caída de la bomba
tiempo_caida = math.sqrt((2 * altura) / gravedad)

# b) Velocidad al impactar
velocidad_vertical = gravedad * tiempo_caida
velocidad_impacto = math.sqrt(velocidad_avion**2 + velocidad_vertical**2)

# c) Distancia recorrida por el barco durante la caída
distancia_barco = velocidad_barco * tiempo_caida

# d) y e) Distancia horizontal entre el avión y el barco
distancia_lanzamiento = velocidad_avion - velocidad_barco
distancia_impacto = distancia_lanzamiento * tiempo_caida

# Mostrar los resultados
print(f"Tiempo de caída: {tiempo_caida:.2f} segundos")
print(f"Velocidad de impacto de la bomba: {velocidad_impacto:.2f} m/s")
print(f"Distancia recorrida por el barco: {distancia_barco:.2f} metros")
print(f"Distancia entre el avión y el barco en el lanzamiento: {distancia_lanzamiento:.2f} metros")
print(f"Distancia entre el avión y el barco en el impacto: {distancia_impacto:.2f} metros")
