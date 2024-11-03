import math

# Datos del problema
m = 1  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
h = 1  # altura en metros

# a) Energía en lo alto de la rampa
U_inicial = m * g * h
K_inicial = 0
E_inicial = U_inicial + K_inicial
print(f"Energía potencial inicial: {U_inicial} J")
print(f"Energía cinética inicial: {K_inicial} J")
print(f"Energía mecánica inicial: {E_inicial} J")

# b) Energías al llegar a la parte horizontal
U_final = 0
K_final = E_inicial
E_final = U_final + K_final
print(f"Energía potencial final: {U_final} J")
print(f"Energía cinética final: {K_final} J")
print(f"Energía mecánica final: {E_final} J")

# c) Velocidad al llegar al suelo
v_final = math.sqrt(2 * K_final / m)
print(f"Velocidad al llegar al suelo: {v_final} m/s")
