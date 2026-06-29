select
    empleado_id,
    nombre,
    apellidos,
    departamento_id,
    departamento,
    puesto,
    fecha_alta,
    salario_bruto_anual,
    activo
from {{ ref('stg_rrhh_empleados') }}
