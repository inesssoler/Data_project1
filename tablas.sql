-- Database
DROP DATABASE IF EXISTS data_project;

CREATE DATABASE data_project;

\c data_project


-- Eliminar tablas anteriores
DROP TABLE IF EXISTS Solicitudes;
DROP TABLE IF EXISTS Destinos;
DROP TABLE IF EXISTS Preferencias;

-- Table: esquema."Solicitudes"

CREATE TABLE Solicitudes
(
    index bigint,
    "Nombre" text COLLATE pg_catalog."default",
    "Apellidos" text COLLATE pg_catalog."default",
    "Edad" bigint,
    "Provincia en la que reside" text COLLATE pg_catalog."default",
    "Telefono" text COLLATE pg_catalog."default",
    "Indique si presenta alguna discapacidad" boolean,
    "Número de la seguridad social" text COLLATE pg_catalog."default",
    "¿Es usted soltero o viudo?" boolean,
    "Indique si vive en una residencia de mayores" boolean,
    "Indique si viajará con acompañante" boolean,
    "Indique si el año pasado disfrutó de algún viaje" boolean,
    "Indique si en 2021 disfrutó de algún viaje" boolean,
    "Importe de su pensión percibida" bigint,
    "Porcentaje de discapacidad" bigint
);

ALTER TABLE Solicitudes
    OWNER TO postgres;

-- Index: ix_esquema_Solicitudes_index

CREATE INDEX ix_Solicitudes_index
    ON Solicitudes USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;



-- Table: esquema."DESTINOS"

-- DROP TABLE esquema."DESTINOS";

CREATE TABLE Destinos
(
    index bigint,
    "Destino" text COLLATE pg_catalog."default",
    "Tipo de destino" bigint,
    indice bigint
)

TABLESPACE pg_default;

ALTER TABLE Destinos
    OWNER to postgres;

-- Index: ix_esquema_DESTINOS_index

-- DROP INDEX esquema."ix_esquema_DESTINOS_index";

CREATE INDEX "ix_Destinos_index"
    ON Destinos USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;


-- Table: esquema."Preferencias"

-- DROP TABLE esquema."Preferencias";

CREATE TABLE Preferencias
(
    index bigint,
    "índice" bigint,
    "Opcion1" text COLLATE pg_catalog."default",
    "Opcion2" text COLLATE pg_catalog."default",
    "Opcion3" text COLLATE pg_catalog."default",
    "Opcion4" text COLLATE pg_catalog."default",
    "Opcion5" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE Preferencias
    OWNER to postgres;

-- Index: ix_esquema_Preferencias_index

-- DROP INDEX esquema."ix_esquema_Preferencias_index";

CREATE INDEX "ix_Preferencias_index"
    ON Preferencias USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;

