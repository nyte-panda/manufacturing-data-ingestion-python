import psycopg2
from psycopg2.extras import execute_batch
import pandas as pd


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="manufacturing",
        user="postgres",
        password="postgres"
    )


def insert_production_runs(df: pd.DataFrame):
    """
    Insert production run records into PostgreSQL.
    """

    insert_sql = """
        INSERT INTO production_runs (
            run_id,
            work_order_id,
            machine_id,
            operator_id,
            start_time,
            end_time
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    records = df[
        [
            "run_id",
            "work_order_id",
            "machine_id",
            "operator_id",
            "start_time",
            "end_time",
        ]
    ].values.tolist()

    conn = get_connection()
    cur = conn.cursor()

    try:
        execute_batch(cur, insert_sql, records)
        conn.commit()
    finally:
        cur.close()
        conn.close()
