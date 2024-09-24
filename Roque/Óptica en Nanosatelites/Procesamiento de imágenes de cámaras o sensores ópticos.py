import cv2
import numpy as np

# Leer la imagen desde el sensor (archivo simulado aquí)
img = cv2.imread('imagen_sensor_nanosatelite.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro de realce (filtro de alta frecuencia)
img_filtered = cv2.GaussianBlur(img, (5, 5), 0)
img_sharpened = cv2.addWeighted(img, 1.5, img_filtered, -0.5, 0)

# Mostrar imagen antes y después
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Realzada', img_sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
