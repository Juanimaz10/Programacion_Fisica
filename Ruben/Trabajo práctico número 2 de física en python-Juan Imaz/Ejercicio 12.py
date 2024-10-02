# Datos
d = 600  # Distancia en metros
t = 15  # Tiempo en segundos

# a) Aceleración (usamos la fórmula: d = 0.5 * a * t^2)
a = (2 * d) / (t**2)

# b) Velocidad final (usamos la fórmula: v_final = a * t)
v_final = a * t

# Convertimos la velocidad a km/h
v_final_kmh = v_final * 3600 / 1000

# Mostramos los resultados
print(f"Aceleración: {a:.2f} m/s²")
print(f"Velocidad de despegue: {v_final_kmh:.2f} km/h")
