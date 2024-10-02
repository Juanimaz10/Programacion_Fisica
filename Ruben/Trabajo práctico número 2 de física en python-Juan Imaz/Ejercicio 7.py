# Datos
v_inicial_kmh = 15  # Velocidad inicial en km/h
v_final_kmh = 50  # Velocidad final en km/h
t = 13  # Tiempo en segundos

# Convertimos las velocidades a m/s
v_inicial_ms = v_inicial_kmh * 1000 / 3600
v_final_ms = v_final_kmh * 1000 / 3600

# a) Aceleración
a = (v_final_ms - v_inicial_ms) / t

# b) Distancia recorrida (usamos la fórmula: d = v_inicial * t + 0.5 * a * t^2)
d = v_inicial_ms * t + 0.5 * a * t**2

# Mostramos los resultados
print(f"Aceleración: {a:.2f} m/s²")
print(f"Distancia recorrida: {d:.2f} metros")
