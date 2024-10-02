# Datos
distancia_total = 200  # Distancia San Juan - Luján en km
distancia_mendoza = 160  # Distancia San Juan - Mendoza en km
tiempo_total = 4  # Tiempo total en horas (8 a.m. a 12 p.m.)

# Tiempo que tarda en pasar por Mendoza
tiempo_mendoza = (distancia_mendoza / distancia_total) * tiempo_total

# Hora en que pasó por Mendoza
hora_salida = 8  # Hora de salida
hora_mendoza = hora_salida + tiempo_mendoza

# Mostramos el resultado
print(f"El auto pasó por Mendoza a las {hora_mendoza:.2f} a.m.")
