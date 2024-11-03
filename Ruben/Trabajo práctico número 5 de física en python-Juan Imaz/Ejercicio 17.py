import math

# Datos del problema
m = 2  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
t = 3  # tiempo en segundos

# a) Velocidad máxima alcanzada
v_max = g * t
print(f"Velocidad máxima alcanzada: {v_max} m/s")

# b) Altura desde donde se soltó
h = (1/2) * g * t**2
print(f"Altura desde donde se soltó: {h} m")

# c) Energía potencial, cinética y mecánica inicial
U_inicial = m * g * h
K_inicial = 0
E_inicial = U_inicial + K_inicial
print(f"Energía potencial inicial: {U_inicial} J")
print(f"Energía cinética inicial: {K_inicial} J")
print(f"Energía mecánica inicial: {E_inicial} J")

# d) Energías justo antes de tocar el suelo
U_final = 0
K_final = E_inicial
E_final = U_final + K_final
print(f"Energía potencial final: {U_final} J")
print(f"Energía cinética final: {K_final} J")
print(f"Energía mecánica final: {E_final} J")
