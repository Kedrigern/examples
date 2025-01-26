"""
Simple work with DuckDB
duckdb.execute() -- vrátí con, například pro navazující dotazy
duckdb.sql() -- vrací objekt relace, který reprezentuje výsledek dotazu.
"""

import duckdb as dd

con: dd.DuckDBPyConnection = dd.connect(':memory:')

stm1: str = """
CREATE TABLE people (
    id int,
    name varchar(255)
);
INSERT INTO people VALUES 
(1, 'Mark'),
(2, 'John'),
(3, 'Stan');
"""
stm2: str = "SELECT * FROM people"
stm3: str = "SELECT id FROM people"
stm4: str = "INSERT INTO people2 VALUES"

print(type(con))
con.execute(stm1)           # Create and insert

names: dd.DuckDBPyRelation = con.sql(stm2)

print(type(names))
print(names)             # Graphical string
print(names.fetchall())  # Python objects
print(names.df())        # Pandas dataframe     

ids = con.sql(stm3)
print(ids.fetchnumpy())  # Numpy object

try:
    con.execute(stm4)
except dd.ParserException:
    print("Invalid SQL")
