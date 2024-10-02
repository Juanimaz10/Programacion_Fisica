# Velocidad de la luz en metros por segundo
velocidad_luz_m_s = 3e8

# 1 parpadeo = 3e17 attosegundos (as), 1 as = 1e-18 segundos
parpadeo_as = 3e17
parpadeo_s = parpadeo_as * 1e-18

# Velocidad de la luz en metros por parpadeo
velocidad_luz_m_parpadeo = velocidad_luz_m_s * parpadeo_s

# Distancia recorrida por la luz en un parpadeo
distancia_luz_parpadeo = velocidad_luz_m_s * parpadeo_s

# Resultados
print(f"Velocidad de la luz en metros por parpadeo: {velocidad_luz_m_parpadeo} m/parpadeo")
print(f"Distancia recorrida por la luz en un parpadeo: {distancia_luz_parpadeo} metros")
