import pandas as pd
import matplotlib.pyplot as plt


def load_data() -> pd.DataFrame:

    body = [(1, 1), (1.5, 1.5), (2, 2), (3, 3)]

    # Převod na DataFrame pro lepší práci s daty
    # Jinak je třeba rozeskat body po osách: `x = np.array([1, 1.5, 2, 3])`
    return pd.DataFrame(body, columns=['x', 'y'])


def load_data_csv() -> pd.DataFrame:
    return pd.read_csv('../data/dots.lin.csv')


def draw_graph(df: pd.DataFrame, label: str = 'Graph') -> None:
    plt.figure(figsize=(8, 6), num=label)
    plt.scatter(df['x'], df['y'], color='blue', label='Body')

    # plt.savefig('../img/vis-dots.png')

    plt.show()


def main() -> None:
    df = load_data()

    print("\nData z kódu jako DataFrame:")
    print(df)

    draw_graph(df, 'Vizualizace bodových dat z kódu')


    df = load_data_csv()

    print("\nData z CSV jako DataFrame:")
    print(df)

    draw_graph(df, 'Vizualizace bodových dat z csv')    


if __name__ == '__main__':
    main()