g = 9.8  # gravedad en m/s^2

def problema_13():
    m_A = 4  # kg
    m_B = 8  # kg
    mu = 0.25  # coeficiente de rozamiento
    N_A = m_A * g  # Normal sobre A
    N_B = m_B * g  # Normal sobre B
    F_rozamiento_A = mu * N_A
    F_rozamiento_B = mu * N_B
    # Fuerza necesaria para arrastrar B
    P_necesaria = F_rozamiento_B + F_rozamiento_A
    return P_necesaria

print("Problema 13:", problema_13())
