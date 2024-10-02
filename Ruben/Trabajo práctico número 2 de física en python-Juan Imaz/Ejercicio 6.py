# Datos
distancia_km = 1  # Distancia en km
tiempo_min = 4  # Tiempo en minutos

# a) Velocidad en km/h
vel_kmh = distancia_km / (tiempo_min / 60)

# b) Velocidad en pies/s (1 km = 3280.84 pies)
distancia_pies = distancia_km * 3280.84
tiempo_seg = tiempo_min * 60
vel_pies_s = distancia_pies / tiempo_seg

# c) Velocidad en millas/h (1 km = 0.621371 millas)
distancia_millas = distancia_km * 0.621371
vel_millas_h = distancia_millas / (tiempo_min / 60)

# d) Velocidad en cm/s (1 km = 100000 cm)
distancia_cm = distancia_km * 100000
vel_cm_s = distancia_cm / tiempo_seg

# Mostramos los resultados
print(f"Velocidad media en km/h: {vel_kmh:.2f}")
print(f"Velocidad media en pies/s: {vel_pies_s:.2f}")
print(f"Velocidad media en millas/h: {vel_millas_h:.2f}")
print(f"Velocidad media en cm/s: {vel_cm_s:.2f}")
