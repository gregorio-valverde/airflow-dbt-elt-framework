from __future__ import annotations
from include.elt.config.extractors.extract import extract_src_rrhh_nominas, extract_src_rrhh_consultoras, extract_src_rrhh_departamentos, extract_src_rrhh_evaluaciones, extract_src_rrhh_personal

pipelines = [
    {
        "pipeline_id": "nominas",
        "yaml_path": "/usr/local/airflow/include/elt/config/src/src_rrhh_nominas.yml",
        "extractor": extract_src_rrhh_nominas,
        "sync_enabled": True,
        "load_mode_default": "massive",
        "enabled": True,
    },
    {
        "pipeline_id": "consultoras",
        "yaml_path": "/usr/local/airflow/include/elt/config/src/src_rrhh_consultoras.yml",
        "extractor": extract_src_rrhh_consultoras,
        "sync_enabled": True,
        "load_mode_default": "massive",
        "enabled": True,
    },
    {
        "pipeline_id": "departamentos",
        "yaml_path": "/usr/local/airflow/include/elt/config/src/src_rrhh_departamentos.yml",
        "extractor": extract_src_rrhh_departamentos,
        "sync_enabled": True,
        "load_mode_default": "massive",
        "enabled": True,
    },
    {
        "pipeline_id": "evaluaciones",
        "yaml_path": "/usr/local/airflow/include/elt/config/src/src_rrhh_evaluaciones.yml",
        "extractor": extract_src_rrhh_evaluaciones,
        "sync_enabled": True,
        "load_mode_default": "massive",
        "enabled": True,
    },
    {
        "pipeline_id": "personal",
        "yaml_path": "/usr/local/airflow/include/elt/config/src/src_rrhh_personal.yml",
        "extractor": extract_src_rrhh_personal,
        "sync_enabled": True,
        "load_mode_default": "massive",
        "enabled": True,
    },
]
