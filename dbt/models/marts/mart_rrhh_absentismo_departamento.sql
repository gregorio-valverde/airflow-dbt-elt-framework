select
    departamento_id,
    departamento,
    date_trunc('month', fecha_inicio)::date as mes,
    count(*) as total_ausencias,
    count(distinct empleado_id) as empleados_con_ausencia,
    sum(dias_ausencia) as dias_ausencia,
    sum(coste_estimado) as coste_estimado
from {{ ref('fct_rrhh_absentismo') }}
group by 1, 2, 3
