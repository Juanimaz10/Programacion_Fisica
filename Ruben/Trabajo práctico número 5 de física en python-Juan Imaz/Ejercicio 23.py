import matplotlib.pyplot as plt
import math
# Datos del problema
m = 4  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
U_inicial = 6000  # Energía potencial inicial en J

# a) Identificación de curvas
print("La curva descendente es la energía potencial y la curva ascendente es la energía cinética.")

# b) Altura desde donde se soltó
h0 = U_inicial / (m * g)
print(f"Altura inicial: {h0} m")

# c) Velocidad máxima
K_final = U_inicial
v_max = math.sqrt(2 * K_final / m)
print(f"Velocidad máxima: {v_max} m/s")

# d) Energía a los 1.5 s (dependiendo de los valores aproximados del gráfico)
U_1_5s = 4500  # Ejemplo
K_1_5s = 1500  # Ejemplo
E_1_5s = U_1_5s + K_1_5s
print(f"Energía total a 1.5 s: {E_1_5s} J")

# e) Justificación de caída en vacío
print("La conservación de la energía indica que el cuerpo cae en el vacío.")


# Datos aproximados del problema (tiempo en segundos y energía en julios)
tiempo = [0, 1, 2, 3, 4, 5, 6]  # tiempo en segundos
energia_potencial = [6000, 5000, 4000, 3000, 2000, 1000, 0]  # energía potencial en julios
energia_cinetica = [0, 1000, 2000, 3000, 4000, 5000, 6000]  # energía cinética en julios
energia_mecanica = [6000] * len(tiempo)  # energía mecánica total (constante)

# Graficamos los datos
plt.figure(figsize=(10, 6))
plt.plot(tiempo, energia_potencial, label="Energía Potencial (U)", color="blue", marker='o')
plt.plot(tiempo, energia_cinetica, label="Energía Cinética (K)", color="magenta", marker='s')
plt.plot(tiempo, energia_mecanica, label="Energía Mecánica Total (E)", color="green", linestyle="--")
plt.xlabel("Tiempo (s)")
plt.ylabel("Energía (J)")
plt.title("Energías en función del Tiempo para el Ejercicio 23")
plt.legend()
plt.grid()
plt.show()
