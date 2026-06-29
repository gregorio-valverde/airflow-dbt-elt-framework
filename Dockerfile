FROM astrocrpublic.azurecr.io/runtime-dev:3.1-5

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER astro

ENV DBT_PROFILES_DIR=/usr/local/airflow/dbt

RUN pip install --no-cache-dir \
    dbt-core==1.9.0 \
    dbt-postgres==1.9.0 \
    psycopg2-binary \
    pandas \
    sqlalchemy \
    apache-airflow-providers-postgres
