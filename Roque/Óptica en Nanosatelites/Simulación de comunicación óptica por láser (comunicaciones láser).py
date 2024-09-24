import numpy as np

# Parámetros de la señal
frecuencia = 10e9  # 10 GHz
velocidad_luz = 3e8  # m/s

# Función de transmisión óptica
def transmitir_datos(dato, potencia, distancia):
    atenuación = np.exp(-0.01 * distancia)  # Atenuación simple
    potencia_recibida = potencia * atenuación
    return dato if potencia_recibida > 1e-3 else None

# Simulación de transmisión
dato_enviado = "Hola desde el satélite"
potencia_transmitida = 10  # en Watts
distancia_satelite = 500e3  # 500 km

dato_recibido = transmitir_datos(dato_enviado, potencia_transmitida, distancia_satelite)

if dato_recibido:
    print(f"Datos recibidos: {dato_recibido}")
else:
    print("Se perdió la señal.")