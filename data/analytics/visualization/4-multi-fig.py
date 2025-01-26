import matplotlib.pyplot as plt
import numpy as np

# Vytvoření figury s rozložením 1 řádek a 3 sloupce
# sharey = sdílení os
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# První graf: Jeden bod
axes[0].plot(1, 1, 'ro')
axes[0].set_title("Jeden bod")

# Druhý graf: Čára
x = np.linspace(0, 10, 100) # 100 prvků rovnoměrně od 0 do 10
y = np.sin(x)               # sinus hodnot pro předešlé prvky
axes[1].plot(x, y)
axes[1].set_title("Čára")

# Třetí graf: Dva body
axes[2].plot([1, 2], [1, 2], 'bo')
axes[2].set_title("Dva body")

# Nastavení mezer mezi subplots
plt.tight_layout()

plt.savefig('../img/vis-multi-fig.png')
plt.show()