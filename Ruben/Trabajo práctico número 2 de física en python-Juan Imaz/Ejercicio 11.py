# Datos
v_inicial_kmh = 100  # Velocidad inicial en km/h
g = 9.81  # Aceleración de la gravedad en m/s²
a_frenado = 0.8 * g  # Desaceleración en m/s²

# Convertimos la velocidad a m/s
v_inicial_ms = v_inicial_kmh * 1000 / 3600
v_final = 0  # Se detiene

# Distancia de frenado (usamos la fórmula: v_final^2 = v_inicial^2 + 2 * a * d)
d_frenado = (v_final**2 - v_inicial_ms**2) / (2 * -a_frenado)

# Tiempo de reacción
t_reaccion = 0.75  # En segundos
d_reaccion = v_inicial_ms * t_reaccion

# Distancia total
d_total = d_frenado + d_reaccion

# Mostramos los resultados
print(f"Distancia de frenado: {d_frenado:.2f} metros")
print(f"Distancia total con tiempo de reacción: {d_total:.2f} metros")
