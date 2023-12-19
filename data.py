import json
import random
from faker import Faker
import unidecode
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

fake = Faker('es_ES')

num_registros = 500

base_de_datos = []

# Crear registros individualmente
for _ in range(num_registros):
    datos = {
        'Nombre': fake.name(),
        'Apellidos': fake.last_name(),
        'Edad': random.randint(60, 99),
        'Provincia': fake.state(),
        'Telefono': fake.phone_number(),
        'Discapacitado': fake.boolean(),
        'Numero de la seguridad social': fake.ssn(),
        'Es usted soltero o viudo': fake.boolean(),
        'Indique si vive en una residencia de mayores': fake.boolean(),
        'Indique si viajara con acompañante': fake.boolean(),
        'Indique si el año pasado disfruto de algun viaje': fake.boolean(),
        'Importe de la pension': round(random.uniform(480,3000))
        
    }
    if datos['Discapacitado'] == True:
        datos['Porcentaje de discapacidad'] = round(random.uniform(1,85))
    else:
        datos['Porcentaje de discapacidad'] = 0
    
# Añadir los registros individuales a la lista
    base_de_datos.append(datos)

# Crear un DataFrame a partir de la lista
# Las tildes se muestran bien
    df = pd.DataFrame(base_de_datos)


# Guardar la base de datos en un archivo JSON
with open('base_de_datos.json', 'w') as archivo:
    json.dump(base_de_datos, archivo, indent=2)

print("Base de datos generada y guardada en 'base_de_datos.json'")


# Paso de df a SQL
# Conectar a la base de datos 'postgres' (DB del sistema) para crear la nueva 'data_project'
#engine = create_engine('postgresql+psycopg2://postgres:Welcome01@127.0.0.1/postgres', pool_recycle=5050)
connection_target = psycopg2.connect(
        host='Postgres',
        database='postgres',
        user='postgres',
        password='Welcome01',
        port=5432
    )
cur_target = conn_target.cursor()
#postgres_connection = engine.connect()
data_project = 'data_project'
cur_target.execute('''CREATE DATABASE {data_project}''')
#Cerrar la conexión a la BD 'postgres'

#postgres_connection = engine.connect()
#cur_target = postgres_connection.cursor()

#postgres_solicitudes = 'Solicitudes'
#dframe1 = df.to_sql(postgres_solicitudes, postgres_connection, if_exists = 'replace')
