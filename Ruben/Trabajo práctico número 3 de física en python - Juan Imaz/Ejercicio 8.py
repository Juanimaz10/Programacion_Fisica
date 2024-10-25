import math

# Datos del problema
velocidad_plato_kmh = 36  # km/h
distancia_horizontal = 17  # m
altura_tirador = 1.8  # m
velocidad_bala = 20  # m/s
gravedad = 9.8  # m/s^2

# Convertir velocidad del plato a m/s
velocidad_plato = velocidad_plato_kmh / 3.6

# a) Ángulo de inclinación de la escopeta
angulo_inclinacion = math.degrees(math.atan(altura_tirador / distancia_horizontal))

# b) Tiempo de vuelo de la bala
tiempo_bala = distancia_horizontal / velocidad_bala

# Altura del plato al impactar
altura_impacto = velocidad_plato * tiempo_bala - 0.5 * gravedad * tiempo_bala**2

# Mostrar los resultados
print(f"Ángulo de inclinación de la escopeta: {angulo_inclinacion:.2f} grados")
print(f"Altura a la que se produce el impacto: {altura_impacto:.2f} metros")
