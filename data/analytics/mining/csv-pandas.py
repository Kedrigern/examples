"""
"""
import numpy as np
import pandas as pd

filename: str = '../data/gdp-per-capita-2024.csv'
df: pd.DataFrame = pd.read_csv(filename)

print('Data z CSV: ')
print(df)

print('---')

print('Druhý a pátý řádek:')
print(df.loc[[2,4]])


print('---')

print('Filtrování:')
# Boolean vektor, který se nazývá maska, používá se pro filtrování
mask: pd.Series = df['Country Name'] == 'Czechia'  
czechia: pd.DataFrame = df[mask]
print(czechia)
gdp2023: np.float64 = czechia['2023'].round(2).iloc[0]
print(f'GDP Czechia 2023 {gdp2023} {type(gdp2023)}')