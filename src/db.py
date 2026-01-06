import getpass
import os

import psycopg2
from psycopg2.extras import execute_batch
import pandas as pd


def get_connection():
    dsn = os.getenv("DATABASE_URL")
    if dsn:
        return psycopg2.connect(dsn)

    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        database=os.getenv("PGDATABASE", "manufacturing"),
        user=os.getenv("PGUSER", getpass.getuser()),
        password=os.getenv("PGPASSWORD", ""),
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
        ON CONFLICT (run_id) DO NOTHING
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
