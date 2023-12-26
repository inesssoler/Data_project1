-- Create esquema

CREATE SCHEMA IF NOT EXISTS esquema;


-- Table: esquema."Solicitudes"

CREATE TABLE esquema.solicitudes
(
    solicitud_id bigint PRIMARY KEY,
    nombre varchar(50),
    apellidos text COLLATE pg_catalog."default",
    edad smallint,
    provincia_residente varchar(50),
    telefono numeric(9,0),
    discapacidad boolean,
    seguridad_social numeric(12,0),
    soltero_o_viudo boolean,
    vive_en_residencia boolean,
    viajara_con_acompanante boolean,
    imserso_anopasado boolean,
    imserso_2021 boolean,
    importe_pension smallint,
    porcentaje_discapacidad tinyint,
    CONSTRAINT solcitudes_pkey PRIMARY KEY (solicitud_id)
);


-- Table: esquema."destinos"
CREATE TABLE esquema.destinos
(
    index bigint,
    destino text COLLATE pg_catalog."default",
    tipo_destino tinyint,
    CONSTRAINT destinos_pkey PRIMARY KEY (tipo_destino),
    CONSTRAINT tdestino_fkey FOREIGN KEY (tipo_destino) REFERENCES esquema.tdestino(tipo_destino)
);

-- Table: esquema."preferencias"
CREATE TABLE esquema.preferencias
(
    solicitud_id bigint PRIMARY KEY,
    opcion_n tinyint,
    ciudad text COLLATE pg_catalog "default",
    CONSTRAINT preferencias_pkey PRIMARY KEY (solicitud_id)
);

-- Table: esquema."tipo de destino"
CREATE TABLE esquema.tdestino
(
    tipo_destino tinyint PRIMARY KEY,
    duracion text COLLATE pg_catalog."default",
    CONSTRAINT tdestino_pkey PRIMARY KEY (tipo_destino)
);


-- Table: esquema."hoteles"
CREATE TABLE esquema.hoteles
(
    hotel_id bigint PRIMARY KEY,
    ciudad text COLLATE pg_catalog "default",
    hotel text COLLATE pg_catalog "default"
)