import math

# Datos del problema
aceleracion = 19.6  # m/s^2
tiempo_aceleracion = 60  # s
gravedad = 9.8  # m/s^2

# a) Primera fase (aceleración constante)
velocidad_final = aceleracion * tiempo_aceleracion
distancia_aceleracion = 0.5 * aceleracion * tiempo_aceleracion**2

# b) Segunda fase (movimiento libre)
tiempo_adicional = velocidad_final / gravedad
distancia_libre = velocidad_final * tiempo_adicional - 0.5 * gravedad * tiempo_adicional**2

# Altura máxima
altura_maxima = distancia_aceleracion + distancia_libre

# c) Tiempo total de vuelo
tiempo_caida = math.sqrt(2 * altura_maxima / gravedad)
tiempo_total = tiempo_aceleracion + tiempo_adicional + tiempo_caida

# Mostrar los resultados
print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
print(f"Tiempo total de vuelo: {tiempo_total:.2f} segundos")
