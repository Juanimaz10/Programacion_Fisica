import math

# Datos del problema
v_y0 = 24  # m/s (componente vertical inicial)
v_x0 = 30  # m/s (componente horizontal inicial)
gravedad = 9.8  # m/s^2

# a) Posición y velocidad en 2 s, 3 s, y 6 s
tiempos = [2, 3, 6]
posiciones = []
velocidades = []
velocidades_x = []  # Para almacenar la velocidad horizontal constante

for t in tiempos:
    # Posición
    y = v_y0 * t - 0.5 * gravedad * t**2
    x = v_x0 * t
    posiciones.append((x, y))
    
    # Velocidad vertical y total
    v_y = v_y0 - gravedad * t
    v_total = math.sqrt(v_x0**2 + v_y**2)
    velocidades.append(v_total)
    
    # Velocidad horizontal constante
    velocidades_x.append(v_x0)

# b) Tiempo para alcanzar el punto más alto
t_max = v_y0 / gravedad

# c) Altura máxima
y_max = v_y0 * t_max - 0.5 * gravedad * t_max**2

# d) Tiempo total de vuelo (el doble del tiempo para alcanzar el punto más alto)
t_total = 2 * t_max

# e) Distancia horizontal total
x_total = v_x0 * t_total

# Imprimir resultados
print("Posiciones y velocidades en los tiempos especificados:")
for i, t in enumerate(tiempos):
    print(f"A {t} segundos: posición (x = {posiciones[i][0]:.2f} m, y = {posiciones[i][1]:.2f} m), velocidad = {velocidades[i]:.2f} m/s, velocidad horizontal = {velocidades_x[i]:.2f} m/s")

print(f"\nTiempo para alcanzar el punto más alto: {t_max:.2f} segundos")
print(f"Altura máxima alcanzada: {y_max:.2f} metros")
print(f"Tiempo total de vuelo: {t_total:.2f} segundos")
print(f"Distancia horizontal total: {x_total:.2f} metros")


