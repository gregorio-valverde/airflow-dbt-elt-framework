import pandas as pd
from sqlalchemy import text
from pathlib import Path

from include.connections.postgres.client import PostgresClient


class PostgresSelectReader:
    """
    Lector de consultas SELECT en PostgreSQL leyendo el SQL desde un archivo.

    Uso:
        reader = PostgresSelectReader(conn_id="dw_postgres")
        df = reader.read("/ruta/consulta.sql", vars={"schema": "raw"})
    """

    def __init__(self, conn_id: str):
        self.conn_id = conn_id
        self.engine = PostgresClient(conn_id).sqlalchemy_engine()

    def read(self, sql_path: str, vars: dict | None = None) -> pd.DataFrame:
        path = Path(sql_path)
        if not path.exists():
            raise FileNotFoundError(f"No existe el archivo SQL: {sql_path}")

        sql_raw = path.read_text(encoding="utf-8")
        sql = sql_raw.format(**vars) if vars else sql_raw

        sql_clean = sql.lstrip()
        sql_upper = sql_clean.upper()

        if sql_upper.startswith("WITH "):
            if "SELECT" not in sql_upper:
                raise ValueError("La consulta con CTE debe contener un SELECT.")
        elif not sql_upper.startswith("SELECT"):
            raise ValueError("Solo se permiten consultas SELECT o WITH + SELECT en este reader.")

        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)
