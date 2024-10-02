# Conversión de 180.32 pie/seg a otras unidades

# Dato de velocidad en pie/seg
velocidad_ft_s = 180.32

# Conversión a metros por segundo (1 pie = 0.3048 metros)
velocidad_m_s = velocidad_ft_s * 0.3048

# Conversión a millas por hora (1 pie/seg = 0.681818 mph)
velocidad_mph = velocidad_ft_s * 0.681818

# Conversión a millas por segundo (1 pie/seg = 0.000189394 millas/seg)
velocidad_mill_s = velocidad_ft_s * 0.000189394

# Conversión a kilómetros por hora (1 pie/seg = 1.09728 km/h)
velocidad_km_h = velocidad_ft_s * 1.09728

# Resultados
print(f"Velocidad en m/s: {velocidad_m_s}")
print(f"Velocidad en millas/h: {velocidad_mph}")
print(f"Velocidad en millas/s: {velocidad_mill_s}")
print(f"Velocidad en km/h: {velocidad_km_h}")
