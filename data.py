#---------------------------------------------------------------------------------------------------------------------------------------
import json
import random
from faker import Faker
import pandas as pd
from sqlalchemy import create_engine, text 
import psycopg2
import unicodedata

# Adapta la librería 'Faker' al español castellano con nombres en dicho idioma
fake = Faker('es_ES')

# Cantidad de solicitantes a generar
num_registros = 1000

# Tabla generada de las solicitudes
base_de_datos = []

# Crea los registros de forma individual
for _ in range(num_registros):
    datos = {
        'Nombre': fake.first_name(),
        'Apellidos': fake.last_name(),
        'Edad': random.randint(60, 99),
        'Provincia en la que reside': fake.state(),
        'Telefono': fake.phone_number(),
        'Indique si presenta alguna discapacidad': fake.boolean(),
        'Número de la seguridad social': fake.ssn(),
        '¿Es usted soltero o viudo?': fake.boolean(),
        'Indique si vive en una residencia de mayores': fake.boolean(),
        'Indique si viajará con acompañante': fake.boolean(),
        'Indique si el año pasado disfrutó de algún viaje': fake.boolean(),
        'Indique si en 2021 disfrutó de algún viaje': fake.boolean(),
        'Importe de su pensión percibida': round(random.uniform(480,3000))
    }
    if datos['Indique si presenta alguna discapacidad'] == True:
        datos['Porcentaje de discapacidad'] = round(random.uniform(1,85))
    else:
        datos['Porcentaje de discapacidad'] = 0
    
# Añade los registros a la lista
    base_de_datos.append(datos)

# Crea un DataFrame a partir de la lista
    df = pd.DataFrame(base_de_datos)

#Guarda la base de datos en un JSON con codificación utf-8 y ensure_ascii=False, facilitando las tildes e imprimiéndolo por pantalla
with open('base_de_datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(base_de_datos, archivo, indent=2, ensure_ascii=False)

print("Base de datos generada y guardada en 'base_de_datos.json'")
<<<<<<< HEAD
#------------------------------------------------------------------------------------------------------------------------------------------

# Paso de df a SQL
# Conectar a la base de datos 'postgres' (DB del sistema) para crear la nueva 'data_project'
engine = create_engine('postgresql+psycopg2://postgres:Welcome01@127.0.0.1/postgres')
'''
##connection_target = psycopg2.connect(
        ##host='Postgres',
        ##database='postgres',
        ##user='postgres',
        ##password='Welcome01',
        ##port=5432
    ##)
    ##''' 
#cur_target = conn_target.cursor()
postgres_connection = engine.connect()
with engine.connect() as postgres_connection:
    postgres_connection.execution_options(isolation_level="AUTOCOMMIT")
    query = text ('CREATE DATABASE data_project')
    postgres_connection.execute(query)
#Cerrar la conexión a la BD 'postgres'
postgres_connection.close()


#Abrir DB data_project e insertar tabla 'Solicitudes'
engine2 = create_engine('postgresql+psycopg2://postgres:Welcome01@127.0.0.1/data_project')
postgres_connection2 = engine2.connect()
esquema = 'esquema'
postgres_solicitudes = 'Solicitudes'
query2 = text('CREATE SCHEMA IF NOT EXISTS esquema')
postgres_connection2.execute(query2)
dframe1 = df.to_sql(postgres_solicitudes, postgres_connection2, schema=esquema, if_exists = 'replace')
query3 = text('COMMIT')
postgres_connection2.execute(query3)




#cur_target = postgres_connection.cursor()
#, pool_recycle=5050
=======
#---------------------------------------------------------------------------------------------------------------------------------------
>>>>>>> main
