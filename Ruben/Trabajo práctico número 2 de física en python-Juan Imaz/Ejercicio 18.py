# Datos
a_cohete = 19.6  # Aceleración del cohete en m/s²
t_combustible = 60  # Tiempo en segundos durante el cual el cohete acelera

# a) Altura máxima alcanzada
# Velocidad cuando se acaba el combustible
v_final = a_cohete * t_combustible

# Altura alcanzada durante el ascenso con combustible (usamos la fórmula: d = 0.5 * a * t^2)
h_combustible = 0.5 * a_cohete * t_combustible**2

# Altura alcanzada después de que se acaba el combustible (usamos la fórmula: v_final^2 = 2 * g * h)
g = 9.81  # Aceleración de la gravedad en m/s²
h_libre = (v_final**2) / (2 * g)

# Altura total
h_total = h_combustible + h_libre

# b) Tiempo total hasta que regresa a la Tierra
# Tiempo de ascenso después de que se agota el combustible
t_libre = v_final / g

# Tiempo de caída libre (es el mismo que el tiempo de ascenso libre)
t_caida = t_libre

# Tiempo total
t_total = t_combustible + t_libre + t_caida

# Mostramos los resultados
print(f"Altura máxima alcanzada: {h_total:.2f} metros")
print(f"Tiempo total hasta regresar a la Tierra: {t_total:.2f} segundos")
