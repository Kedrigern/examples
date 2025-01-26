import pandas as pd
import duckdb as dd

filepath: str = "../data/w3schools2.sql"

con  = dd.connect()

type(con)

with open(filepath, 'r') as f:
    sql: str = f.read()
    con.sql(sql)

# con.ex

# df = pd.read_sql()
