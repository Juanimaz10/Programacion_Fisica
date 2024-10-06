import math 
# Datos del problema
v_0 = 300  # m/s
angulo = 30  # grados
gravedad = 9.8  # m/s^2

# a) Alcance máximo
theta = math.radians(angulo)
alcance = (v_0**2 * math.sin(2 * theta)) / gravedad

# b) Altura máxima
altura_maxima = (v_0**2 * math.sin(theta)**2) / (2 * gravedad)

# c) Velocidad a los 10 segundos
t = 10
v_x = v_0 * math.cos(theta)
v_y = v_0 * math.sin(theta) - gravedad * t
velocidad_total = math.sqrt(v_x**2 + v_y**2)

# Mostrar los resultados
print(f"Alcance máximo: {alcance:.2f} metros")
print(f"Altura máxima: {altura_maxima:.2f} metros")
print(f"Velocidad a los 10 segundos: {velocidad_total:.2f} m/s")
