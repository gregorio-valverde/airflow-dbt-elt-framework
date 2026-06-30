import yaml

def read_columns_yaml_list(yaml_path: str) -> list[str]:
    """
    Lee las columnas (atributo 'name') desde un YAML y devuelve
    una lista con los nombres en orden.
    """
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    columns = data.get("columns", [])
    if not isinstance(columns, list):
        raise ValueError("El YAML debe contener una lista en la clave 'columns'.")

    return [col["name"] for col in columns if "name" in col]
