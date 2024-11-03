# Datos del problema
m = 16  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
h0 = 20  # altura inicial en metros

# Energía mecánica total
E_total = m * g * h0
print(f"Energía mecánica total: {E_total} J")

# Energías en diferentes alturas
alturas = [20, 15, 10, 5, 0]
for h in alturas:
    U = m * g * h
    K = E_total - U
    print(f"Altura: {h} m - Energía potencial: {U} J - Energía cinética: {K} J")
