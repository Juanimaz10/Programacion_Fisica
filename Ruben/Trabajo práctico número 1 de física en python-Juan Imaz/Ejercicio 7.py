# Conversión de unidades

# a) 0.053 m² a cm² (1 m² = 1e4 cm²)
area_m2 = 0.053
area_cm2 = area_m2 * 1e4

# b) 470 mL a m³ (1 mL = 1e-6 m³)
volumen_mL = 470
volumen_m3 = volumen_mL * 1e-6

# c) 2130 m² a hectáreas (1 ha = 1e4 m²)
area_m2_ha = 2130
area_ha = area_m2_ha / 1e4

# d) 230 mL a cm³ (1 mL = 1 cm³)
volumen_mL_cm3 = 230
volumen_cm3 = volumen_mL_cm3  # 1 mL = 1 cm³

# e) 24000 mm³ a m³ (1 mm³ = 1e-9 m³)
volumen_mm3 = 24000
volumen_m3_mm3 = volumen_mm3 * 1e-9

# f) 300 cm³ a litros (1 L = 1000 cm³)
volumen_cm3_l = 300
volumen_L = volumen_cm3_l / 1000

# g) 120000 cm³ a mm³ (1 cm³ = 1000 mm³)
volumen_cm3_mm3 = 120000
volumen_mm3_g = volumen_cm3_mm3 * 1000

# h) 4000 mm³ a litros (1 mm³ = 1e-6 L)
volumen_mm3_l = 4000
volumen_L_mm3 = volumen_mm3_l * 1e-6

# Resultados
print(f"0.053 m² en cm²: {area_cm2}")
print(f"470 mL en m³: {volumen_m3}")
print(f"2130 m² en hectáreas: {area_ha}")
print(f"230 mL en cm³: {volumen_cm3}")
print(f"24000 mm³ en m³: {volumen_m3_mm3}")
print(f"300 cm³ en litros: {volumen_L}")
print(f"120000 cm³ en mm³: {volumen_mm3_g}")
print(f"4000 mm³ en litros: {volumen_L_mm3}")
