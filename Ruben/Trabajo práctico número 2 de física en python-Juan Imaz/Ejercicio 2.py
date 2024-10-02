# Definimos las velocidades
v1 = 40  # Velocidad del auto más lento en m/s
v2 = 60  # Velocidad del auto más rápido en m/s

# Distancia inicial entre los autos (asumimos que empiezan juntos)
d = 200  # Distancia entre los autos en metros

# Tiempo hasta que el auto rápido alcance al más lento
t = d / (v2 - v1)

# Mostramos el resultado
print(f"El tiempo en que el auto más rápido alcanza al otro es de {t:.2f} segundos.")
