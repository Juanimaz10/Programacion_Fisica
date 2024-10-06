import math 
# Datos del problema
distancia_horizontal = 23  # m
altura_inicial = 2  # m
angulo = 45  # grados
gravedad = 9.8  # m/s^2

# a) Tiempo en el aire
# Fórmula: d = v_x * t, despejar t
v_0 = math.sqrt((distancia_horizontal * gravedad) / math.sin(2 * math.radians(angulo)))

# b) Altura máxima
t_max = (v_0 * math.sin(math.radians(angulo))) / gravedad
altura_max = altura_inicial + (v_0 * math.sin(math.radians(angulo)) * t_max) - 0.5 * gravedad * t_max**2

# Mostrar resultados
print(f"Velocidad inicial: {v_0:.2f} m/s")
print(f"Altura máxima: {altura_max:.2f} m")
 