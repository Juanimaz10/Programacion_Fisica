import math 
# Datos del problema
velocidad_plato_kmh = 36  # km/h
distancia_horizontal = 17  # m
altura_tirador = 1.8  # m
gravedad = 9.8  # m/s^2

# Convertir velocidad del plato a m/s
velocidad_plato = velocidad_plato_kmh * 1000 / 3600

# a) Ángulo de inclinación de la escopeta
angulo_inclinacion = math.degrees(math.atan(altura_tirador / distancia_horizontal))

# Mostrar los resultados
print(f"Ángulo de inclinación de la escopeta: {angulo_inclinacion:.2f} grados")
