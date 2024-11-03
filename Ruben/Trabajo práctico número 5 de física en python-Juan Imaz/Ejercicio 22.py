import math 

# Datos del problema
m = 4  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
E_total = m * g * 6  # energía total en el punto A (altura 6 m)

# Energías y velocidades en cada punto
puntos = {"A": 6, "B": 0, "C": 4, "D": 2}
for punto, h in puntos.items():
    U = m * g * h
    K = E_total - U
    v = math.sqrt(2 * K / m)
    print(f"Punto {punto} - Altura: {h} m - Energía potencial: {U} J - Energía cinética: {K} J - Velocidad: {v} m/s")
