import laspy
import matplotlib.pyplot as plt

# Cargar un archivo de datos LIDAR
file = laspy.read("datos_lidar.las")

# Extraer los puntos
points = np.vstack((file.x, file.y, file.z)).transpose()

# Graficar una vista simple de los datos LIDAR
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap='viridis')
plt.show()
