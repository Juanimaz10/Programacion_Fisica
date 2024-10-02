# Datos
a_auto = 1.8  # Aceleración del auto en m/s²
v_camion = 9  # Velocidad del camión en m/s

# a) Distancia donde el auto alcanza al camión
# Usamos: d_auto = 0.5 * a * t^2 y d_camion = v_camion * t
# Igualamos las distancias para encontrar t
from sympy import symbols, Eq, solve

t = symbols('t')
eq = Eq(0.5 * a_auto * t**2, v_camion * t)
t_sol = solve(eq)[0]

# Distancia donde el auto alcanza al camión
d = v_camion * t_sol

# b) Velocidad del auto en ese instante
v_auto = a_auto * t_sol

# Mostramos los resultados
print(f"Distancia donde el automóvil alcanza al camión: {d:.2f} metros")
print(f"Velocidad del automóvil en ese instante: {v_auto:.2f} m/s")
