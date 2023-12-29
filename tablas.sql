-- Table: "Solicitudes"
CREATE TABLE "solicitudes"
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

-- Table: "destinos"
CREATE TABLE "destinos"
(
    tipo_destino_id smallint PRIMARY KEY,
    tipo_destino text,
    duracion text
);

-- Table: "ciudades"
CREATE TABLE "ciudades"
(
    ciudades_id bigint PRIMARY KEY,
    ciudad text,
    tipo_destino_id smallint,
    CONSTRAINT fk_tipo_destino
    FOREIGN KEY (tipo_destino_id)
    REFERENCES destinos(tipo_destino_id)
);


-- Table: "preferencias"
CREATE TABLE "preferencias"
(
    preferencias_id bigint PRIMARY KEY,
    opcion_1 text,
    opcion_2 text,
    opcion_3 text,
    opcion_4 text,
    opcion_5 text,
    opcion_id_1 bigint,
    opcion_id_2 bigint,
    opcion_id_3 bigint,
    opcion_id_4 bigint,
    opcion_id_5 bigint,
    solicitud_id bigint,
    FOREIGN KEY (opcion_id_1) REFERENCES ciudades(ciudades_id),
    FOREIGN KEY (opcion_id_2) REFERENCES ciudades(ciudades_id),
    FOREIGN KEY (opcion_id_3) REFERENCES ciudades(ciudades_id),
    FOREIGN KEY (opcion_id_4) REFERENCES ciudades(ciudades_id),
    FOREIGN KEY (opcion_id_5) REFERENCES ciudades(ciudades_id),
    FOREIGN KEY (solicitud_id) REFERENCES solicitudes(solicitud_id)
);


-- Table: "hoteles"
CREATE TABLE "hoteles"
(
    hotel_id bigint PRIMARY KEY,
    hotel text,
    ciudad text,
    ciudades_id bigint,
    CONSTRAINT fk_ciudad
    FOREIGN KEY (ciudades_id)
    REFERENCES ciudades(ciudades_id)
);

