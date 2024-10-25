import math

# Datos del problema
altura = 8  # m
velocidad_inicial = 10.0  # m/s
angulo = 20  # grados
gravedad = 9.8  # m/s^2

# Componentes de la velocidad inicial
v_x = velocidad_inicial * math.cos(math.radians(angulo))
v_y = velocidad_inicial * math.sin(math.radians(angulo))

# Resolviendo la ecuación cuadrática para el tiempo de vuelo
# Ecuación: (1/2) * g * t^2 + v_y * t - h = 0
a = 0.5 * gravedad
b = v_y
c = -altura

# Solución de la ecuación cuadrática
discriminante = b**2 - 4 * a * c
if discriminante >= 0:
    t1 = (-b + math.sqrt(discriminante)) / (2 * a)
    t2 = (-b - math.sqrt(discriminante)) / (2 * a)
    # El tiempo válido es el positivo
    tiempo_vuelo = max(t1, t2)

    # Distancia horizontal recorrida
    distancia_horizontal = v_x * tiempo_vuelo

    # Mostrar los resultados
    print(f"Tiempo de vuelo: {tiempo_vuelo:.2f} segundos")
    print(f"Distancia horizontal desde la ventana: {distancia_horizontal:.2f} metros")
else:
    print("No hay solución real.")
 