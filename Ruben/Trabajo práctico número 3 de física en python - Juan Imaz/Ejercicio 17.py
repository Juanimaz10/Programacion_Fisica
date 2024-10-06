# Datos del problema
profundidad = 125  # m
tiempo_salida = 2.15  # s
gravedad = 9.8

# a) Aceleración constante
aceleracion = (2 * profundidad) / (tiempo_salida**2)

# b) Velocidad al salir del agua
velocidad_salida = aceleracion * tiempo_salida

# c) Altura máxima alcanzada fuera del agua
altura_maxima = (velocidad_salida**2) / (2 * gravedad)

# Mostrar los resultados
print(f"Aceleración del cohete: {aceleracion:.2f} m/s^2")
print(f"Velocidad al salir del agua: {velocidad_salida:.2f} m/s")
print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
