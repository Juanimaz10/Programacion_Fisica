import math

# Datos del problema
v_0 = 37.0  # m/s (velocidad inicial)
angulo = 53.1  # grados
gravedad = 9.8  # m/s^2

# Componentes de la velocidad inicial
v_x = v_0 * math.cos(math.radians(angulo))
v_y = v_0 * math.sin(math.radians(angulo))

# a) Posición y velocidad a t = 2 s
t = 2
x = v_x * t
y = v_y * t - 0.5 * gravedad * t**2
v_y_t = v_y - gravedad * t
v_total = math.sqrt(v_x**2 + v_y_t**2)
angulo_velocidad = math.degrees(math.atan(v_y_t / v_x))

# b) Tiempo para alcanzar el punto más alto
t_max = v_y / gravedad

# Altura máxima
y_max = v_y * t_max - 0.5 * gravedad * t_max**2

# c) Tiempo total de vuelo y alcance horizontal
t_total = 2 * t_max
alcance_horizontal = v_x * t_total

# Mostrar los resultados
print(f"Posición a t = 2 s: x = {x:.2f} m, y = {y:.2f} m")
print(f"Velocidad a t = 2 s: {v_total:.2f} m/s, con ángulo {angulo_velocidad:.2f}°")
print(f"Tiempo para el punto más alto: {t_max:.2f} s")
print(f"Altura máxima: {y_max:.2f} m")
print(f"Alcance horizontal: {alcance_horizontal:.2f} m")
