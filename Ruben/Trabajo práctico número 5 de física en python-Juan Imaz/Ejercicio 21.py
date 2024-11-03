import matplotlib.pyplot as plt
import numpy as np

# Parámetros dados
h_inicial = 10.0  # Altura inicial en metros (puedes ajustar este valor)
m = 4.0           # Masa del objeto en kg
g = 9.81          # Aceleración de la gravedad en m/s^2

# Calcular el tiempo total de caída usando la fórmula t_total = sqrt(2 * h_inicial / g)
t_total = np.sqrt(2 * h_inicial / g)

# Crear un rango de tiempos desde 0 hasta t_total con 100 puntos
tiempos = np.linspace(0, t_total, 100)

# Calcular la altura en función del tiempo: h(t) = h_inicial - (1/2) * g * t^2
alturas_t = h_inicial - 0.5 * g * tiempos**2

# Calcular las energías en función del tiempo
U_t = m * g * alturas_t                    # Energía potencial
K_t = m * g * h_inicial - U_t              # Energía cinética
E_mecanica_t = U_t + K_t                   # Energía mecánica total (constante)

# Graficar las energías en función del tiempo
plt.figure(figsize=(10, 6))
plt.plot(tiempos, U_t, label="Energía Potencial (U)", color="blue")
plt.plot(tiempos, K_t, label="Energía Cinética (K)", color="red")
plt.plot(tiempos, E_mecanica_t, label="Energía Mecánica Total (E)", color="green", linestyle="--")

# Personalizar los ejes y el título del gráfico
plt.xlabel("Tiempo (s)")
plt.ylabel("Energía (J)")
plt.title("Energías en función del Tiempo")
plt.legend()
plt.grid(True)
plt.show()

