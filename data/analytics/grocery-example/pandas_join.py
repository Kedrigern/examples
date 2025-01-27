import pandas as pd

df1 = pd.DataFrame([
    {'id': 1, 'price': 200, 'item_id': 1},
    {'id': 2, 'price': 100, 'item_id': 2},
    {'id': 3, 'price': 190, 'item_id': 1}
]).set_index('id')

df2 = pd.DataFrame([
    {'id': 1, 'name': 'Lorem ipsum'},
    {'id': 2, 'name': 'Dolorem'}
]).set_index('id')

print(df1)
print(df2)

df3 = df1.join(df2, on='item_id')[['price', 'name']]

print(df3)