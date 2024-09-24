# Instalación del módulo pyrayoptics
# !pip install pyrayoptics

from pyrayoptics import ray_tracer

# Definir las propiedades de la lente (foco, distancia, etc.)
lens = ray_tracer.Lens(focal_length=100, diameter=50)

# Definir las propiedades del rayo
ray = ray_tracer.Ray(angle=0.05, position=10)

# Realizar el trazado del rayo a través de la lente
ray_path = ray_tracer.trace_ray_through_lens(lens, ray)

# Mostrar resultados
ray_tracer.plot_ray_path(ray_path)