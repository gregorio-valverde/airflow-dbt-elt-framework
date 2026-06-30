from pathlib import Path

import pandas as pd


def _get_data_dir() -> Path:
    """
    Localiza la carpeta include/data desde cualquier ubicación del archivo extract.py.
    Esto evita depender de rutas absolutas.
    """
    current_path = Path(__file__).resolve()

    for parent in current_path.parents:
        candidate = parent / "include" / "data"
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No se ha encontrado la carpeta include/data desde la ubicación del archivo extract.py"
    )


def _read_csv(filename: str) -> pd.DataFrame:
    """
    Lee un CSV desde include/data y devuelve un DataFrame.
    No transforma, no limpia y no normaliza.
    """
    data_dir = _get_data_dir()
    file_path = data_dir / filename

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo CSV: {file_path}")

    return pd.read_csv(file_path)


def extract_src_rrhh_personal(dag=None, etl_vars=None, **kwargs) -> pd.DataFrame:
    """
    Extrae el origen raw de personal.
    Tabla destino esperada: raw.src_rrhh_personal
    """
    return _read_csv("personal.csv")


def extract_src_rrhh_departamentos(dag=None, etl_vars=None, **kwargs) -> pd.DataFrame:
    """
    Extrae el origen raw de departamentos.
    Tabla destino esperada: raw.src_rrhh_departamentos
    """
    return _read_csv("departamentos.csv")


def extract_src_rrhh_consultoras(dag=None, etl_vars=None, **kwargs) -> pd.DataFrame:
    """
    Extrae el origen raw de consultoras.
    Tabla destino esperada: raw.src_rrhh_consultoras
    """
    return _read_csv("consultoras.csv")


def extract_src_rrhh_evaluaciones(dag=None, etl_vars=None, **kwargs) -> pd.DataFrame:
    """
    Extrae el origen raw de evaluaciones.
    Tabla destino esperada: raw.src_rrhh_evaluaciones
    """
    return _read_csv("evaluaciones.csv")


def extract_src_rrhh_nominas(dag=None, etl_vars=None, **kwargs) -> pd.DataFrame:
    """
    Extrae el origen raw de nóminas 2025.
    Tabla destino esperada: raw.src_nominas_2025
    """
    return _read_csv("nominas.csv")