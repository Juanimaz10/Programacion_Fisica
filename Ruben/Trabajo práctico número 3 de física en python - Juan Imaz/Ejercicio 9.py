import math

# Datos del problema
altura_inicial = 2.50  # m
altura_final = 3.05  # m
distancia_horizontal = 6.25  # m
angulo = 37  # grados
gravedad = 9.8  # m/s^2

# Convertir ángulo a radianes
theta = math.radians(angulo)

# Ecuación para el tiempo de vuelo
def calcular_velocidad_inicial(altura_inicial, altura_final, distancia_horizontal, gravedad, theta):
    # Fórmula para el tiempo de vuelo basado en la componente horizontal
    a = -0.5 * gravedad * (distancia_horizontal / math.cos(theta))**2
    b = distancia_horizontal * math.tan(theta)
    c = altura_inicial - altura_final

    # Resolver la ecuación cuadrática
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        return None  # No hay solución real
    else:
        v0 = (-b + math.sqrt(discriminante)) / (2 * a)
        return v0

# Calcular la velocidad inicial
velocidad_inicial = calcular_velocidad_inicial(altura_inicial, altura_final, distancia_horizontal, gravedad, theta)

# Mostrar los resultados
if velocidad_inicial:
    print(f"Velocidad inicial del balón: {velocidad_inicial:.2f} m/s")
else:
    print("No hay solución real.")
