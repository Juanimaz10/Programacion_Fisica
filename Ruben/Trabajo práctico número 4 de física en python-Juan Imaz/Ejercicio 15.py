import numpy as np

g = 9.8  # gravedad en m/s^2

def problema_15():
    m_horizontal = 280  # kg
    m_inclinado = 700  # kg
    theta = np.radians(30)  # conversión de grados a radianes
    # Aceleración del sistema
    F_paralela = m_inclinado * g * np.sin(theta)
    F_sujecion = m_horizontal * g  # Fuerza necesaria para sujetar el sistema
    a_sistema = F_paralela / (m_horizontal + m_inclinado)
    return a_sistema, F_sujecion


a_sistema, F_sujecion = problema_15()
print("Aceleración del sistema: {:.2f} m/s^2".format(a_sistema))
print("Fuerza de sujeción: {:.2f} N".format(F_sujecion))
