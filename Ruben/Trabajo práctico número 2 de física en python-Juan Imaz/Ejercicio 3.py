# Suponemos que t es el tiempo que tarda normalmente en llegar al trabajo
# Si al ir al doble de velocidad llega una hora antes, el tiempo es la mitad
# Entonces, el tiempo normal es 2 horas (porque al ir al doble tarda 1 hora)

t_lento = 2  # Horas que tarda normalmente
hora_llegada_normal = 9  # Hora de llegada habitual

# Hora de salida
hora_salida = hora_llegada_normal - t_lento

# Mostramos el resultado
print(f"Normalmente sale de su casa a las {hora_salida}:00 a.m.")
