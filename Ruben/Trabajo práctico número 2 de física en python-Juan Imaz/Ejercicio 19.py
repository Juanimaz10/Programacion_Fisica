# Datos
g = 9.81  # Aceleración de la gravedad en m/s²
t_retraso = 1  # Retraso de 1 segundo entre las piedras
v_inicial_piedra2 = 18  # Velocidad inicial de la segunda piedra en m/s

# Usamos las fórmulas de distancia recorrida en caída libre
# Piedra 1: d1 = 0.5 * g * t^2
# Piedra 2: d2 = v_inicial_piedra2 * t + 0.5 * g * t^2
# La segunda piedra alcanzará a la primera cuando d1 = d2

from sympy import symbols, Eq, solve

t = symbols('t')
d1 = 0.5 * g * (t + t_retraso)**2
d2 = v_inicial_piedra2 * t + 0.5 * g * t**2

# Planteamos la ecuación d1 = d2
eq = Eq(d1, d2)
t_sol = solve(eq)[0]  # Solución para el tiempo en que se alcanzan

# Distancia a la que se alcanzan
d_alcance = 0.5 * g * (t_sol + t_retraso)**2

# Mostramos los resultados
print(f"La segunda piedra alcanzará a la primera en {d_alcance:.2f} metros")
