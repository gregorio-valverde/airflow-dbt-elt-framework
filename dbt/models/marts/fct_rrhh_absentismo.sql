select
    a.ausencia_id,
    a.empleado_id,
    e.departamento_id,
    e.departamento,
    e.puesto,
    a.fecha_inicio,
    a.fecha_fin,
    a.tipo_ausencia,
    a.dias_ausencia,
    a.coste_estimado,
    current_date as fecha_modelado
from {{ ref('stg_rrhh_absentismo') }} a
left join {{ ref('stg_rrhh_empleados') }} e
    on a.empleado_id = e.empleado_id
