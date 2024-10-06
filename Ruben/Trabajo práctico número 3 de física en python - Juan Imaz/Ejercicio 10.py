import math
# Datos del problema
altura = 18  # m
velocidad_inicial = 12  # m/s
angulo = 45  # grados
gravedad = 9.8  # m/s^2

# Componentes de la velocidad inicial
v_x = velocidad_inicial * math.cos(math.radians(angulo))

# a) Tiempo de caída (caída libre)
tiempo_caida = math.sqrt((2 * altura) / gravedad)

# b) Distancia horizontal recorrida
distancia_horizontal = v_x * tiempo_caida

# c) Velocidad al impactar
v_y = gravedad * tiempo_caida
velocidad_total = math.sqrt(v_x**2 + v_y**2)

# Mostrar los resultados
print(f"Tiempo de caída: {tiempo_caida:.2f} segundos")
print(f"Distancia horizontal desde el borde del tejado: {distancia_horizontal:.2f} metros")
print(f"Velocidad al impactar el suelo: {velocidad_total:.2f} m/s")
