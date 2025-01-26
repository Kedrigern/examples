import pandas as pd


df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})

ax = df.plot.bar(x='lab', y='val', rot=0)

exit

ser = pd.Series([1, 2, 3, 3])
plot = ser.plot(kind='hist', title="My plot")

body = [(1, 1), (1.5, 1.5), (2, 2), (3, 3)]

# Převod na DataFrame pro lepší práci s daty
# Jinak je třeba rozeskat body po osách: `x = np.array([1, 1.5, 2, 3])`
df = pd.DataFrame(body, columns=['x', 'y'])

print(df)

df.plot(kind='line')