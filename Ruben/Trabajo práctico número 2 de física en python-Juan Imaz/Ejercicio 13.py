# Datos
d = 54  # Distancia en metros
t = 6  # Tiempo en segundos
v_final = 13.5  # Velocidad en m/s al final

# a) Aceleración (usamos la fórmula: d = v_inicial * t + 0.5 * a * t^2)
# Despejamos v_inicial usando la ecuación de velocidad final: v_final = v_inicial + a * t
# Entonces: v_inicial = v_final - a * t
v_inicial = (2 * d / t) - v_final

# Aceleración
a = (v_final - v_inicial) / t

# Mostramos los resultados
print(f"Aceleración: {a:.2f} m/s²")
print(f"Velocidad en el primer punto: {v_inicial:.2f} m/s")
