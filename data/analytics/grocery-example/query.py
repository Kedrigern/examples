import duckdb as dd
from duckdb.typing import DuckDBPyConnection
import pandas as pd

def get_con() -> DuckDBPyConnection:
    db_file = 'data/data.db'
    return dd.connect(db_file, read_only=True)


def basic_query(con: DuckDBPyConnection) -> None:
    stmt1: str = "SELECT * FROM order;"

    res: dd.DuckDBPyRelation = con.sql(stmt1)

    res.show()                          # Show data in terminal

    data1: list[any] = res.fetchall()   # Data as python list[tuple]
    data2: pd.DataFrame = res.df()

    print(data1)
    print(data2)


def pandas_example(con: DuckDBPyConnection) -> None:
    stmt1: str = "SELECT * FROM product;"
    stmt2: str = "SELECT * FROM purchase;"
    stmt3: str = "SELECT * FROM order;"

    prod: pd.DataFrame = con.sql(stmt1).df().set_index('id')
    purch: pd.DataFrame = con.sql(stmt2).df().set_index('id')
    view: pd.DataFrame = con.sql(stmt3).df().set_index('id')

    #print(view)

    joined = purch.join(prod, on="article")

    df = joined[
        ['uuid', 'purchase_id', 'long_description', 'i_quantity', 'i_measurement', 'price_per_item', 'price_item_total', 'price']
        ].rename(columns={'uuid': 'customer', 'long_description': 'description', 'i_quantity': 'quantity', 'i_measurement': 'measurement'})

    print("Joined:")
    print(df)


    mask = df['purchase_id'] == 104
    order_104 = df[mask]
    sum = order_104['price_item_total'].sum()
    print(f'Order 104 (sum CZK: {sum}):')
    print(order_104)

    customer = 'c1799f82-b43c-45c2-8255-8aa869b582f6'
    mask = df['customer'] == customer
    purchase_c17 = df[mask]
    count = purchase_c17[['purchase_id']].value_counts()
    print(f'Customer {customer} has {count} orders')


def main():
    try:
        with get_con() as con:
            # basic_query(con)
            pandas_example(con)
    except dd.IOException:
        print("[error] Probably cannot lock the file")

if __name__ == "__main__":
    main()
