create schema if not exists raw;

create table if not exists raw.src_rrhh_personal (
    fecha_extraccion date,
    sistema_origen text,
    archivo_origen text,
    nro_linea_archivo integer,
    legajo integer,
    nombre text,
    apellido text,
    departamento_codigo text,
    departamento_descripcion text,
    tipo_empleado text,
    salario numeric(14,2),
    precio_hora numeric(14,2),
    precio_hora_extra numeric(14,2),
    consultora_cuit text,
    consultora_razon_social text,
    evaluacion_2024 text,
    evaluacion_2023 text,
    evaluacion_2022 text,
    evaluacion_2021 text,
    evaluacion_2020 text,
    rotacion integer
);

create table if not exists raw.src_rrhh_departamentos (
    departamento_codigo text,
    departamento_descripcion text,
    activo text,
    fecha_extraccion date,
    sistema_origen text
);

create table if not exists raw.src_rrhh_consultoras (
    consultora_cuit text,
    consultora_razon_social text,
    estado_proveedor text,
    fecha_extraccion date,
    sistema_origen text
);

create table if not exists raw.src_rrhh_evaluaciones (
    sistema_origen text,
    fecha_extraccion date,
    nro_linea_archivo integer,
    legajo integer,
    nombre text,
    apellido text,
    departamento_codigo text,
    anio_evaluacion integer,
    resultado_evaluacion text
);

create table if not exists raw.src_nominas_2025 (
    sistema_origen text,
    fecha_extraccion date,
    recibo_nomina_id text,
    periodo text,
    legajo integer,
    nombre text,
    apellido text,
    departamento_codigo text,
    tipo_empleado text,
    consultora_cuit text,
    estado_liquidacion text,
    dias_liquidados integer,
    salario_mensual numeric(14,2),
    horas_base numeric(10,2),
    importe_horas_base numeric(14,2),
    horas_extra numeric(10,2),
    importe_horas_extra numeric(14,2),
    bono_productividad numeric(14,2),
    descuento_ausencias numeric(14,2),
    total_bruto numeric(14,2),
    coste_empresa_estimado numeric(14,2)
);
