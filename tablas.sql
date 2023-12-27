-- Create esquema
CREATE SCHEMA IF NOT EXISTS esquema;

-- Table: esquema."Solicitudes"
CREATE TABLE esquema."solicitudes"
(
    solicitud_id bigint PRIMARY KEY,
    nombre varchar(50),
    apellidos text,
    edad smallint,
    provincia_residente varchar(50),
    telefono varchar(50),
    discapacidad boolean,
    seguridad_social varchar(50),
    soltero_o_viudo boolean,
    vive_en_residencia boolean,
    viajara_con_acompanante boolean,
    imserso_anopasado boolean,
    imserso_2021 boolean,
    importe_pension smallint,
    porcentaje_discapacidad smallint
);

-- Table: esquema."destinos"
CREATE TABLE esquema."destinos"
(
    index bigint,
    destino text,
    tipo_destino smallint,
    CONSTRAINT destinos_pkey PRIMARY KEY (tipo_destino)
);

-- Table: esquema."preferencias"
CREATE TABLE esquema."preferencias"
(
    solicitud_id bigint PRIMARY KEY,
    opcion_n smallint,
    ciudad text
);

-- Table: esquema."tipo de destino"
CREATE TABLE esquema."tdestino"
(
    tipo_destino smallint PRIMARY KEY,
    duracion text
);

-- Table: esquema."hoteles"
CREATE TABLE esquema."hoteles"
(
    hotel_id bigint PRIMARY KEY,
    ciudad text,
    hotel text
);
