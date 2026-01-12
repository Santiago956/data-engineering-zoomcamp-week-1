import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:postgres@localhost:5433/ny_taxi'
engine = create_engine(conn_string)


df_parquet = pd.read_parquet('data/green_tripdata_2025-11.parquet')
df_parquet.to_sql('tripdata_2025', engine, if_exists='replace', index=False)
