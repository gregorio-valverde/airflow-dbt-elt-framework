import logging
from pathlib import Path

from sqlalchemy import text

from include.connections.postgres.client import PostgresClient


class PostgresUpdateExecutor:
    """
    Ejecuta sentencias UPDATE, DELETE, INSERT, TRUNCATE, CREATE, ALTER, DROP o WITH
    en PostgreSQL leyendo el SQL desde un archivo.
    """

    def __init__(self, conn_id: str):
        self.conn_id = conn_id
        self.engine = PostgresClient(conn_id).sqlalchemy_engine()

    def run(self, sql_path: str, params: dict | None = None):
        if params is None:
            params = {}

        path = Path(sql_path)
        if not path.exists():
            raise FileNotFoundError(f"No existe el archivo SQL: {sql_path}")

        sql_raw = path.read_text(encoding="utf-8")
        sql_clean = sql_raw.lstrip()
        if not sql_clean:
            raise ValueError("El archivo SQL esta vacio.")

        first_word = sql_clean.split()[0].upper()
        allowed = ("UPDATE", "DELETE", "INSERT", "TRUNCATE", "CREATE", "ALTER", "DROP", "WITH")
        if first_word not in allowed:
            raise ValueError(f"Solo se permiten sentencias {allowed} en este executor.")

        with self.engine.begin() as conn:
            result = conn.execute(text(sql_raw), params)
            logging.info(f"Query ejecutada correctamente. Filas afectadas: {result.rowcount}")
            return result.rowcount
