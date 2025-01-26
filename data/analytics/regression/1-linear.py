import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_data() -> pd.DataFrame:
    # df = pd.read_csv('../data/dots.triangle.csv')
    df = pd.read_csv('../data/dots.csv')
    return df

def train_model(X: pd.DataFrame, y: pd.Series) -> LinearRegression:
    """
    X: Nezávislá proměnná (musí být DataFrame), tedy matice
    y: Závislá proměnná
    Model lineární regrese v tomto případě je matematická rovnice přímky, 
    která nejlépe popisuje vztah mezi našimi daty. Model se naučí hodnoty
    pro směrnici a průsečík s osou y této přímky během fáze trénování. 
    Když chceme předpovědět hodnotu pro nové x, jednoduše dosadíme toto x 
    do rovnice přímky a vypočítáme odpovídající y.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def make_prediction(model: LinearRegression, x: float) -> float:
    """Vrátí předpovězenou hodnotu pro osu y pro dané x."""
    values = model.predict([[x]])
    return values[0]

def plot_results(X: pd.DataFrame, y: pd.Series, model: LinearRegression, new_x: float) -> None:
    
    plt.scatter(X, y)               # vykreslí původní data

    pred_line = model.predict(X)    # přímka predikce
    plt.plot(X, pred_line, color='red')      

    pred_point = make_prediction(model, new_x)  # predikce konkrtétního bodu
    plt.scatter(new_x, pred_point, color='green', label=f"Predikce pro x={new_x}")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig('../img/reg-rand-lin.png')
    plt.show()

    print(f"Směrnice (slope): {model.coef_[0]}")
    print(f"Průsečík s osou y: {model.intercept_}")
    print(f"Predikovaná hodnota pro x={new_x}: {pred_point}")

def main() -> None:
    data = load_data()

    # Příprava dat pro model
    X = data[['x']] # Nezávislá proměnná (musí být DataFrame)
    y = data['y']   # Závislá proměnná

    model = train_model(X, y)

    new_x = 3.5 # hodnota pro predikci

    # Predikce a vykreslení
    plot_results(X, y, model, new_x)


if __name__ == "__main__":
    main()