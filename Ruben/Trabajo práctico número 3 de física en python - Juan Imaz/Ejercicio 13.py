# Datos del problema
v_y0 = 25  # m/s (velocidad inicial vertical)
aceleracion_horizontal = 2  # m/s^2
gravedad = 9.8  # m/s^2

# a) Ecuaciones de velocidad y posición
# Vertical
t_max = v_y0 / gravedad  # Tiempo para alcanzar la altura máxima
altura_max = v_y0 * t_max - 0.5 * gravedad * t_max**2

# b) Distancia total
t_total = 2 * t_max
distancia_horizontal = 0.5 * aceleracion_horizontal * t_total**2

# Mostrar los resultados
print(f"Altura máxima: {altura_max:.2f} metros")
print(f"Distancia horizontal recorrida: {distancia_horizontal:.2f} metros")
