import duckdb
import pandas as pd
from sqlalchemy import create_engine

# Export gold data from postgres to a csv.
engine = create_engine('postgresql://your_postgres_user:your_postgres_password@localhost:5432/your_postgres_database') #Replace with your credentials.
gold_df = pd.read_sql_table('gold_sample_data', engine)
gold_df.to_csv('../duckdb/data/gold_sample_data.csv', index=False)

# Connect to DuckDB and query the data.
con = duckdb.connect(database=':memory:', read_only=False)
con.execute("CREATE TABLE gold_data AS SELECT * FROM read_csv_auto('../duckdb/data/gold_sample_data.csv')")

result = con.execute("SELECT name, SUM(total_adjusted_value) FROM gold_data GROUP BY name").fetchdf()
print(result)

con.close()
