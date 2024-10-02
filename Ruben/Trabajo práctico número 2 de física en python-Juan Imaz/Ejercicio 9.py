# Datos
v_inicial_kmh = 45  # Velocidad inicial en km/h
v_final_kmh = 30  # Velocidad final en km/h
d = 80  # Distancia en metros

# Convertimos las velocidades a m/s
v_inicial_ms = v_inicial_kmh * 1000 / 3600
v_final_ms = v_final_kmh * 1000 / 3600

# a) Aceleración (usamos la fórmula: v_final^2 = v_inicial^2 + 2 * a * d)
a = (v_final_ms**2 - v_inicial_ms**2) / (2 * d)

# b) Tiempo transcurrido (usamos la fórmula: v_final = v_inicial + a * t)
t = (v_final_ms - v_inicial_ms) / a

# c) Distancia para detenerse desde 30 km/h (usamos la misma fórmula que en a))
v_final_parada = 0  # Velocidad final en m/s
d_parada = (v_final_parada**2 - v_final_ms**2) / (2 * a)

# Mostramos los resultados
print(f"Aceleración: {a:.2f} m/s² (negativa, ya que es una desaceleración)")
print(f"Tiempo transcurrido: {t:.2f} segundos")
print(f"Distancia para detenerse desde 30 km/h: {d_parada:.2f} metros")
