#!/bin/sh
set -e

# Espera a que el servidor de PostgreSQL esté listo para aceptar conexiones
echo "Esperando a PostgreSQL..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "PostgreSQL está listo para aceptar conexiones."

# Configura el servidor de PgAdmin
echo "Configurando el servidor de PgAdmin..."
python pgadmin_config.py

# Inicia el servidor de PgAdmin
echo "Iniciando el servidor de PgAdmin..."
python pgadmin_server.py
