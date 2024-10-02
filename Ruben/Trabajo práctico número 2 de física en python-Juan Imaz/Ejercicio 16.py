# Datos
v_pasajeros = 30  # Velocidad del tren de pasajeros en m/s
v_carga = 9  # Velocidad del tren de carga en m/s
a_frenado = -1.2  # Desaceleración del tren de pasajeros en m/s²
d_inicial = 180  # Distancia inicial entre los trenes en metros

# Tiempo en que el tren de pasajeros se detendría
t_detencion = v_pasajeros / -a_frenado

# Distancia recorrida por el tren de pasajeros hasta detenerse
d_pasajeros = v_pasajeros * t_detencion + 0.5 * a_frenado * t_detencion**2

# Distancia recorrida por el tren de carga en el mismo tiempo
d_carga = v_carga * t_detencion

# Verificamos si hay choque
if d_pasajeros >= d_inicial + d_carga:
    print("Habrá choque entre los trenes.")
else:
    print("No habrá choque entre los trenes.")
    
# En caso de choque, calculamos dónde ocurre
if d_pasajeros >= d_inicial + d_carga:
    distancia_choque = d_inicial + d_carga
    print(f"El choque ocurrirá a {distancia_choque:.2f} metros desde el punto inicial.")
