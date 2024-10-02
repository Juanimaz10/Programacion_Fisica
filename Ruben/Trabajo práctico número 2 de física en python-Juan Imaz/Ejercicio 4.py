# Datos
v = 36 * 1000 / 3600  # Velocidad en m/s
t = 50  # Tiempo en segundos
L_tunel = 200  # Longitud del túnel en metros

# Distancia recorrida total
d_total = v * t

# Longitud del tren
L_tren = d_total - L_tunel

# Mostramos el resultado
print(f"La longitud del tren es {L_tren:.2f} metros.")
