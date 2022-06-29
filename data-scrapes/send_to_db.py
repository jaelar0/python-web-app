import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def send_to_db(dataframe, table_name, replace):
    conn_string = 'postgresql://postgres:Tigers11@localhost:5432/sportsData'
    engine = create_engine(conn_string)

    dataframe.to_sql(table_name, con=engine, if_exists=replace, index=False)

    conn = psycopg2.connect(conn_string)
    conn.autocommit = True