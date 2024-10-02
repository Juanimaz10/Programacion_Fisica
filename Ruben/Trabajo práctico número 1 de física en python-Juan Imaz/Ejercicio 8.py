# Otras conversiones de unidades

# a) 90 km/h a m/s (1 km/h = 0.27778 m/s)
velocidad_kmh = 90
velocidad_m_s = velocidad_kmh * 0.27778

# b) 2.5 kg/m³ a g/mL (1 kg/m³ = 0.001 g/mL)
densidad_kg_m3 = 2.5
densidad_g_ml = densidad_kg_m3 * 0.001

# c) 30 m/s a km/h (1 m/s = 3.6 km/h)
velocidad_ms = 30
velocidad_kmh_c = velocidad_ms * 3.6

# d) 1.3 g/cm³ a kg/L (1 g/cm³ = 1 kg/L)
densidad_g_cm3 = 1.3
densidad_kg_l = densidad_g_cm3  # 1 g/cm³ = 1 kg/L

# e) 1.2 g/cm³ a kg/m³ (1 g/cm³ = 1000 kg/m³)
densidad_g_cm3_e = 1.2
densidad_kg_m3_e = densidad_g_cm3_e * 1000

# f) 1.3 g/cm² a mg/mm² (1 g/cm² = 10 mg/mm²)
presion_g_cm2 = 1.3
presion_mg_mm2 = presion_g_cm2 * 10

# g) 2500 kg/m³ a g/cm³ (1 kg/m³ = 0.001 g/cm³)
densidad_kg_m3_g = 2500
densidad_g_cm3_g = densidad_kg_m3_g * 0.001

# h) 1.3 kg/cm³ a kg/L (1 kg/cm³ = 1000 kg/L)
densidad_kg_cm3_h = 1.3
densidad_kg_l_h = densidad_kg_cm3_h * 1000

# Resultados
print(f"90 km/h en m/s: {velocidad_m_s}")
print(f"2.5 kg/m³ en g/mL: {densidad_g_ml}")
print(f"30 m/s en km/h: {velocidad_kmh_c}")
print(f"1.3 g/cm³ en kg/L: {densidad_kg_l}")
print(f"1.2 g/cm³ en kg/m³: {densidad_kg_m3_e}")
print(f"1.3 g/cm² en mg/mm²: {presion_mg_mm2}")
print(f"2500 kg/m³ en g/cm³: {densidad_g_cm3_g}")
print(f"1.3 kg/cm³ en kg/L: {densidad_kg_l_h}")
