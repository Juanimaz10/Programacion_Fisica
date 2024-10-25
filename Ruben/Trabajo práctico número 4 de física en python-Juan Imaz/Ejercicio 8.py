g = 9.8  # gravedad en m/s^2

def problema_8():
    m_barra = 50  # kg
    m_hombre = 100  # kg
    W_barra = m_barra * g  # peso de la barra en N
    W_hombre = m_hombre * g  # peso del hombre en N
    # Resolución de las ecuaciones para las tensiones en las cuerdas
    T1 = W_barra / 2  # valor de ejemplo para tensión en la cuerda 1
    T2 = W_hombre / 2  # valor de ejemplo para tensión en la cuerda 2
    return T1, T2

print("Problema 8:", problema_8())