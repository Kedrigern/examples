import matplotlib.pyplot as plt
import numpy as np

# Definice souřadnic pro 4 množiny bodů
data = [
    [(1, 2), (3, 4)],
    [(5, 6), (7, 8)],
    [(9, 10), (11, 12)],
    [(13, 14), (15, 16)]
]

# Barvy, tvary a velikosti pro jednotlivé množiny
colors = ['red', 'green', 'blue', 'purple']
markers = ['o', 's', 'x', '^']
sizes = [100, 200]  # Počáteční a koncová velikost bodů v každé množině
# Dále: průhlednost (alpha), okraje bodů (edgecolors)

# Vytvoření grafu
plt.figure(figsize=(8, 6))

for i, points in enumerate(data):
    x, y = zip(*points)
    # Vytvoření seznamu velikostí pro aktuální množinu
    point_sizes = [sizes[0] + i * (sizes[1] - sizes[0]) for i in range(len(points))]
    plt.scatter(x, y, color=colors[i], marker=markers[i], s=point_sizes, label=f"Množina {i+1}")

plt.legend()
plt.xlabel('Osa x')
plt.ylabel('Osa y')
plt.grid(True)
plt.title('Graf se 4 množinami bodů s různou velikostí')

# plt.savefig('../img/vis-dots-rich.png')

plt.show()

