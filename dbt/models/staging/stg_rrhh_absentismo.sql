select
    ausencia_id,
    empleado_id,
    cast(fecha_inicio as date) as fecha_inicio,
    cast(fecha_fin as date) as fecha_fin,
    trim(tipo_ausencia) as tipo_ausencia,
    cast(dias_ausencia as numeric(10, 2)) as dias_ausencia,
    cast(coste_estimado as numeric(12, 2)) as coste_estimado,
    cast(fecha_carga as timestamp) as fecha_carga
from {{ source('raw_rrhh', 'absentismo') }}
