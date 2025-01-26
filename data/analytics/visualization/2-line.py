"""
Body jsou vykreslovány postupně, čili je třeba je mít seřazené dle x
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data() -> pd.DataFrame:
    body = [(1, 1), (1.5, 1.5), (2, 3), (4,4)]
    return pd.DataFrame(body, columns=['x', 'y'])

def draw_graph(df: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 6), num='Vizualizace přímky z bodů')
    plt.plot(df['x'], df['y'], color='red', label='Přímka')
    plt.scatter(df['x'], df['y'], color='blue', label='Body')

    # plt.savefig('../img/vis-line.png')
    # Pozor na pořadí savefig a show záleží
    plt.show()

def main() -> None:
    df = load_data()

    print("\nData jako DataFrame:")
    print(df)

    draw_graph(df)

if __name__ == '__main__':
    main()
