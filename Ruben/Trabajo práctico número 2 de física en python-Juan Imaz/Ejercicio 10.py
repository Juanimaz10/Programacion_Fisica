# Datos
v_final = 83.8  # Velocidad final en m/s
d = 1.50  # Distancia en metros
v_inicial = 0  # Partimos del reposo

# Aceleración media (usamos la fórmula: v_final^2 = v_inicial^2 + 2 * a * d)
a = (v_final**2 - v_inicial**2) / (2 * d)

# Mostramos el resultado
print(f"La aceleración media es {a:.2f} m/s²")
