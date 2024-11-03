import math

# Datos iniciales del problema
gravedad = 9.8  # m/s^2

# Supongamos que observamos en el gráfico la siguiente información
energia_mecanica_total_24 = 5000  # J, constante en todo el proceso
energia_potencial_inicial_24 = 5000  # J, cuando está en la altura máxima (h inicial)
altura_inicial_24 = 8  # m, altura desde donde se soltó (obtenido del gráfico)

# a) Identificar las curvas de energía
print("La energía mecánica es la línea horizontal constante.")
print("La energía potencial disminuye linealmente con la altura.")
print("La energía cinética aumenta linealmente a medida que disminuye la altura.")

# b) Calcular la altura desde donde se soltó
# Ya está dada en el gráfico como 8 m, pero podríamos verificar con:
altura_calculada_24 = energia_potencial_inicial_24 / (gravedad * 1)  # Suponiendo masa = 1 kg para cálculo general
print(f"Altura inicial calculada (verificación): {altura_calculada_24} m")

# c) Calcular la masa del cuerpo
# Suponiendo que toda la energía potencial inicial está asociada a la altura máxima.
masa_24 = energia_potencial_inicial_24 / (gravedad * altura_inicial_24)
print(f"Masa del cuerpo: {masa_24} kg")

# d) Calcular la velocidad máxima alcanzada
# La velocidad máxima es justo antes de tocar el suelo, donde toda la energía es cinética.
energia_cinetica_maxima_24 = energia_mecanica_total_24  # J
velocidad_maxima_24 = math.sqrt((2 * energia_cinetica_maxima_24) / masa_24)
print(f"Velocidad máxima alcanzada: {velocidad_maxima_24} m/s")

# e) Calcular cuánto demoró la caída
# Usamos la ecuación de caída libre para el tiempo
tiempo_caida_24 = math.sqrt((2 * altura_inicial_24) / gravedad)
print(f"Tiempo de caída: {tiempo_caida_24} s")
