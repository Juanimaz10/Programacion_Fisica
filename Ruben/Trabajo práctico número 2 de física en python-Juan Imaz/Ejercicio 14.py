# Datos
t = 2  # Tiempo en segundos
d = 24  # Distancia en metros
v_final = 14.4  # Velocidad final en m/s

# a) Aceleración (usamos la fórmula: v_final = a * t)
a = v_final / t

# b) Velocidad en el primer punto (es cero porque parte del reposo)
v_inicial = 0  # Parte del reposo

# c) Distancia desde el primer punto al punto de partida
d_inicial = 0.5 * a * t**2

# Mostramos los resultados
print(f"Aceleración: {a:.2f} m/s²")
print(f"Velocidad en el primer punto: {v_inicial} m/s (parte del reposo)")
print(f"Distancia desde el primer punto al punto de partida: {d_inicial:.2f} metros")
