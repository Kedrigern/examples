import duckdb as dd

con = dd.connect(':memory:')

fp_name: str = "../data/dd-name.csv"
fp_hobby: str = "../data/dd-hobby.csv"

stm1 = f"SELECT * FROM '{fp_hobby}';"

print(con.sql(stm1))

stm2 = """
CREATE TABLE hobby (
    id bigint,
    hobyy varchar(255),
    indoor boolean
);"""
con.execute(stm2)
con.execute(f"COPY hobby FROM '{fp_hobby}';")

con.sql("SELECT * FROM hobby").show()

rel = con.from_csv_auto(fp_name)
con.execute("CREATE TABLE name AS SELECT * FROM rel")

con.sql("SHOW ALL TABLES;").show()

res = con.execute("SELECT * FROM name WHERE id = ?", [1])
print(res.fetchall()) # připadně .df()

res = con.execute("SELECT * FROM name WHERE name = $NAME", {'name': 'john'})
print(res.fetchall())


