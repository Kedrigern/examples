import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def load_data() -> pd.DataFrame:
    # df = pd.read_csv('../data/dots.csv')
    df = pd.read_csv('../data/dots.triangle.csv')
    return df

def pol_reg_2(data: pd.DataFrame, X):
    polynomial_features = PolynomialFeatures(degree=2)  # Zvolíme stupeň polynomu (2 pro kvadratickou funkci)
    X_poly = polynomial_features.fit_transform(X)

    # Trénování modelu
    model = LinearRegression()
    model.fit(X_poly, data['y'])

    return model.predict(X_poly)

def main():
    data = load_data()
    X = data['x'].values.reshape(-1, 1)  # Reshape pro správný tvar pro model

    y_pred = pol_reg_2(data, X)

    plt.scatter(X, data['y'])
    plt.plot(X, y_pred, color='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Polynomiální regrese stupně 2")
    plt.savefig('../img/reg-triangle-pol.png')
    plt.show()

if __name__ == '__main__':
    main()
