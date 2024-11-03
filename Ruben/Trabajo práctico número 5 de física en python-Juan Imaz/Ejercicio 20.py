import matplotlib.pyplot as plt
import numpy as np

# Datos del problema
m = 16  # masa en kg
g = 9.8  # aceleración de la gravedad en m/s^2
h_inicial = 20  # altura inicial en metros

# Rango de alturas desde 20 m hasta 0 m
alturas = np.linspace(h_inicial, 0, 100)

# Cálculo de las energías en función de la altura
U = m * g * alturas  # Energía potencial
K = m * g * h_inicial - U  # Energía cinética (conservación de la energía)
E_mecanica = U + K  # Energía mecánica total (constante)

# Gráficos
plt.figure(figsize=(10, 6))
plt.plot(alturas, U, label="Energía Potencial (U)", color="blue")
plt.plot(alturas, K, label="Energía Cinética (K)", color="red")
plt.plot(alturas, E_mecanica, label="Energía Mecánica Total (E)", color="green", linestyle="--")
plt.xlabel("Altura (m)")
plt.ylabel("Energía (J)")
plt.title("Energías en función de la Altura")
plt.legend()
plt.grid()
plt.gca().invert_xaxis()  # Invertimos el eje de altura para que 20 m esté a la izquierda
plt.show()
