import math

# Datos del problema
R = 23  # m (distancia horizontal o alcance)
y_0 = 2  # m (altura inicial)
angulo = 45  # grados
gravedad = 9.8  # m/s^2

# Convertir ángulo a radianes
theta = math.radians(angulo)

# Ecuación cuadrática para resolver el tiempo de vuelo
def resolver_tiempo_y_velocidad(R, y_0, theta, gravedad):
    # Utilizamos la ecuación del alcance para obtener v_0 en función de t
    # R = v_0 * cos(theta) * t -> v_0 = R / (cos(theta) * t)
    
    # Fórmula cuadrática para resolver el tiempo en el aire
    a = -0.5 * gravedad
    b = R * math.tan(theta)
    c = y_0
    
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        # Hay soluciones reales
        t_total = (-b + math.sqrt(discriminante)) / (2 * a)
        
        # Usar el tiempo para encontrar la velocidad inicial
        v_0 = R / (math.cos(theta) * t_total)
        
        return t_total, v_0
    else:
        return None, None

# Resolver para tiempo y velocidad inicial
tiempo_total, velocidad_inicial = resolver_tiempo_y_velocidad(R, y_0, theta, gravedad)

# Calcular la altura máxima (parte c)
def calcular_altura_maxima(v_0, theta, y_0, gravedad):
    # Tiempo para alcanzar la altura máxima
    t_max = (v_0 * math.sin(theta)) / gravedad
    
    # Altura máxima
    y_max = y_0 + v_0 * math.sin(theta) * t_max - 0.5 * gravedad * t_max**2
    return y_max

# Mostrar los resultados
if tiempo_total and velocidad_inicial:
    print(f"Tiempo total en el aire: {tiempo_total:.2f} segundos")
    print(f"Velocidad inicial del peso: {velocidad_inicial:.2f} m/s")
    
    # Calcular y mostrar la altura máxima
    altura_maxima = calcular_altura_maxima(velocidad_inicial, theta, y_0, gravedad)
    print(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")
else:
    print("No se encontraron soluciones reales.")

 