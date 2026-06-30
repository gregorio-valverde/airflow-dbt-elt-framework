# include.connections.postgres

Cliente y endpoints PostgreSQL equivalentes a la estructura `sql_server`.

## Requisitos Python

```txt
psycopg2-binary
sqlalchemy
pandas
pyyaml
apache-airflow-providers-postgres
```

## Estructura esperada en el repo

```text
include/connections/postgres/
├── client.py
└── endpoints/
    ├── select_reader.py
    ├── sync.py
    ├── update_executor.py
    └── writer.py
```

## Conexion Airflow

Ejemplo mediante variable de entorno:

```env
AIRFLOW_CONN_DW_POSTGRES=postgresql://dw_user:dw_password@dw_postgres:5432/dw_rrhh
```

## Uso

```python
from include.connections.postgres.endpoints.sync import PostgresSync
from include.connections.postgres.endpoints.writer import PostgresLoader

PostgresSync("include/etl_config/rrhh/src/src_rrhh_personal.yml", conn_id="dw_postgres").sync()
PostgresLoader("include/etl_config/rrhh/src/src_rrhh_personal.yml", conn_id="dw_postgres").load(df)
```
