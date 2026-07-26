import psycopg2
import logging
import psycopg2.extras as extras
import numpy as np

from config import DB_CONFIG

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def execute_query(query):
    cur = None
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        logging.info("Script has been successfully executed")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        if conn is not None:
            conn.rollback()
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def insert_dataframe(df, table_name):
    df_clean = df.replace({np.nan: None})
    columns = ','.join(list(df_clean.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES %s"
    values = [tuple(x) for x in df_clean.to_numpy()]
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        extras.execute_values(cur, query, values)
        conn.commit()
        logging.info(f"{len(df)} rows have been inserted")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        if conn is not None:
            conn.rollback()
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()