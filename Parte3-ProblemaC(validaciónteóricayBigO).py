import matplotlib.pyplot as plt

# Tamaños de la entrada
n = [1000, 2000, 4000, 8000]

# Tiempos recolectados de tus experimentos
mejor = [0.000129, 0.000273, 0.000618, 0.002223]
promedio = [0.029123, 0.120421, 0.515783, 1.957713]  # <--- Agregados tus datos reales
peor = [0.062366, 0.301380, 1.008412, 4.071922]

# Configuración de las líneas
plt.figure(figsize=(10, 6))
plt.plot(n, mejor, label='Mejor Caso O(n)', marker='o', color='green')
plt.plot(n, promedio, label='Caso Promedio O(n²)', marker='^', color='orange')
plt.plot(n, peor, label='Peor Caso O(n²)', marker='s', color='red')

# Etiquetas y formato
plt.xlabel('Tamaño del arreglo (n)')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparativa de Rendimiento: Insertion Sort')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()
