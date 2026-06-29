select
    empleado_id,
    trim(nombre) as nombre,
    trim(apellidos) as apellidos,
    departamento_id,
    trim(departamento) as departamento,
    trim(puesto) as puesto,
    cast(fecha_alta as date) as fecha_alta,
    cast(salario_bruto_anual as numeric(12, 2)) as salario_bruto_anual,
    cast(activo as boolean) as activo,
    cast(fecha_carga as timestamp) as fecha_carga
from {{ source('raw_rrhh', 'empleados') }}
