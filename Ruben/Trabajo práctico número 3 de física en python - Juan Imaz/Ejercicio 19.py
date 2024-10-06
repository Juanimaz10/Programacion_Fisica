import math

# Datos del problema
v_0_segunda_piedra = 18  # m/s
gravedad = 9.8  # m/s^2

# Igualamos las ecuaciones de movimiento de las dos piedras y resolvemos para t
# La primera piedra: y_1(t) = (1/2) * g * t^2
# La segunda piedra: y_2(t) = v_0 * (t - 1) + (1/2) * g * (t - 1)^2
# Igualamos: (1/2) * g * t^2 = v_0 * (t - 1) + (1/2) * g * (t - 1)^2

# Reescribimos la ecuación como una cuadrática de la forma a*t^2 + b*t + c = 0
a = 0.5 * gravedad
b = -v_0_segunda_piedra - gravedad
c = 0.5 * gravedad - v_0_segunda_piedra

# Resolvemos la ecuación cuadrática usando la fórmula general
discriminante = b**2 - 4 * a * c

if discriminante >= 0:
    # Hay soluciones reales
    t1 = (-b + math.sqrt(discriminante)) / (2 * a)
    t2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    # Elegimos el valor positivo del tiempo (t debe ser mayor que 1)
    t_encuentro = max(t1, t2)
    
    # Calculamos la posición en la que se encuentran (usando la ecuación de la primera piedra)
    y_encuentro = 0.5 * gravedad * t_encuentro**2
    
    # Mostrar los resultados
    print(f"Las dos piedras se encuentran después de {t_encuentro:.2f} segundos")
    print(f"A una distancia de {y_encuentro:.2f} metros debajo del precipicio")
else:
    print("No hay soluciones reales.")
