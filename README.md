# DW RRHH Airflow

Plantilla minima para un proyecto de portfolio con Astronomer, Airflow 3, PostgreSQL y dbt.

## Arquitectura

- Airflow orquesta el flujo.
- PostgreSQL interno de Airflow guarda metadata del orquestador.
- PostgreSQL `dw_postgres` actua como data warehouse analitico.
- dbt transforma datos desde `raw` hacia `staging` y `marts`.

## Puertos

- Airflow API/UI: http://localhost:8080
- Metadata DB de Airflow: localhost:5679
- Data warehouse PostgreSQL: localhost:5433

## Arranque

```bash
astro dev start
```

Para entrar al contenedor:

```bash
astro dev bash
```

Para probar dbt manualmente:

```bash
cd /usr/local/airflow/dbt
dbt debug
dbt run
dbt test
```

## Conexion al data warehouse desde el host

- host: localhost
- port: 5433
- database: dw_rrhh
- user: dw_user
- password: dw_password

## DAG incluido

El DAG `rrhh_seed_and_dbt` crea datos sinteticos de empleados y absentismo en `raw`, ejecuta `dbt run` y despues `dbt test`.

## Modelos dbt incluidos

- `stg_rrhh_empleados`
- `stg_rrhh_absentismo`
- `dim_rrhh_empleado`
- `fct_rrhh_absentismo`
- `mart_rrhh_absentismo_departamento`
