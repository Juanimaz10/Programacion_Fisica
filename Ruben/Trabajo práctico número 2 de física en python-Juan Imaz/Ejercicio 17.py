# Datos
d_horizontal = 100  # Distancia recorrida en cm
t = 4  # Tiempo en segundos
v_inicial = 0  # La pelota parte del reposo

# a) Aceleración (usamos la fórmula: d = 0.5 * a * t^2)
a = (2 * d_horizontal) / t**2

# b) Distancia de descenso vertical (asumimos que la aceleración es constante)
# Usamos trigonometría para encontrar la distancia vertical, suponiendo que la pendiente forma un ángulo
# con el suelo (para simplificar supondremos un ángulo de 45 grados, donde sen(45) = cos(45) = sqrt(2)/2)
import math
angulo = math.radians(45)  # Convertimos a radianes
d_vertical = d_horizontal * math.sin(angulo)

# Mostramos los resultados
print(f"Aceleración de la pelota: {a:.2f} cm/s²")
print(f"Descenso vertical: {d_vertical:.2f} cm")
