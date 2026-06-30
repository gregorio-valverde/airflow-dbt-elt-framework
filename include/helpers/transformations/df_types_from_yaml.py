import yaml
import pandas as pd
import logging

def df_types_from_yaml(df, path_yaml):
    with open(path_yaml, "r") as f:
        spec_yaml = yaml.safe_load(f)

    for col in spec_yaml["columns"]:
        nombre = col["name"]
        tipo = col["type"].upper()
        if nombre not in df.columns:
            continue

        if tipo.startswith("VARCHAR"):
            df[nombre] = df[nombre].astype(object).where(pd.notnull(df[nombre]), None)
        elif tipo == "INT":
            col_values = pd.to_numeric(df[nombre], errors="coerce")
            try:
                df[nombre] = col_values.astype("Int64")
            except (TypeError, ValueError) as e:
                logging.warning(f"[df_types_from_yaml] No se pudo convertir '{nombre}' a Int64: {e}. Se usará float64.")
                df[nombre] = col_values  # Será float64
        elif tipo in ["DATETIME", "DATE"]:
            df[nombre] = pd.to_datetime(df[nombre], errors="coerce")
    return df