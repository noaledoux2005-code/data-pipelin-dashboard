import duckdb

conn = duckdb.connect("data/ecommerce.duckdb")

conn.execute("""CREATE OR REPLACE TABLE raw_orders AS
                    SELECT * FROM read_csv_auto('data/raw_orders.csv')""")

count = conn.execute("SELECT count(*) FROM raw_orders").fetchone()[0]
print(f"Table raw_orders créée avec succès ({count} lignes).")
conn.close 