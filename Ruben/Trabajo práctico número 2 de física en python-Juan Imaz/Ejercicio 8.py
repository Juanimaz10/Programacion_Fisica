# Datos
a_aceleracion = 1.20  # Aceleración en m/s²
t_aceleracion = 10  # Tiempo acelerando en s
t_constante = 30  # Tiempo a velocidad constante en s
a_desaceleracion = -2.40  # Desaceleración en m/s²

# Velocidad máxima alcanzada
v_max = a_aceleracion * t_aceleracion

# Distancia recorrida durante la aceleración
d_aceleracion = 0.5 * a_aceleracion * t_aceleracion**2

# Distancia recorrida durante la velocidad constante
d_constante = v_max * t_constante

# Tiempo para detenerse
t_desaceleracion = v_max / -a_desaceleracion

# Distancia recorrida durante la desaceleración
d_desaceleracion = v_max * t_desaceleracion + 0.5 * a_desaceleracion * t_desaceleracion**2

# Distancia total
d_total = d_aceleracion + d_constante + d_desaceleracion

# Mostramos el resultado
print(f"Distancia total recorrida: {d_total:.2f} metros")
