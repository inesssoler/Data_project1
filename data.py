import json
import random
from faker import Faker
import pandas as pd
import psycopg2

# Adapta la librería 'Faker' al español castellano con nombres en dicho idioma
fake = Faker('es_ES')

# Cantidad de solicitantes a generar
num_registros = 1000

base_de_datos = []

# Crea los registros de forma individual
for _ in range(num_registros):
    datos = {
        'solicitud_id': _ + 1,
        'nombre': fake.first_name(),
        'apellidos': fake.last_name(),
        'edad': random.randint(60, 99),
        'provincia_residente': fake.state(),
        'telefono': fake.phone_number(),
        'discapacidad': fake.boolean(),
        'seguridad_social': fake.ssn(),
        'soltero_o_viudo': fake.boolean(),
        'vive_en_residencia': fake.boolean(),
        'viajara_con_acompanante': fake.boolean(),
        'imserso_anopasado': fake.boolean(),
        'imserso_2021': fake.boolean(),
        'importe_pension': round(random.uniform(480, 3000))
    }
    if datos['discapacidad'] == True:
        datos['porcentaje_discapacidad'] = round(random.uniform(1, 85))
    else:
        datos['porcentaje_discapacidad'] = 0
    
    # Añade los registros a la lista
    base_de_datos.append(datos)

# Crea un DataFrame a partir de la lista
df = pd.DataFrame(base_de_datos)

# Guarda la base de datos en un JSON con codificación utf-8 y ensure_ascii=False, facilitando las tildes e imprimiéndolo por pantalla
with open('base_de_datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(base_de_datos, archivo, indent=2, ensure_ascii=False)

print("Base de datos generada y guardada en 'base_de_datos.json'")

try:
    connection = psycopg2.connect(
        host="localhost",
        database="data_project1",
        user="postgres",
        password="Welcome01"
    )

    cursor = connection.cursor()

    # Itera sobre los datos y ejecuta consultas SQL de inserción
    for datos in base_de_datos:
        insert_query = """
        INSERT INTO esquema.solicitudes 
        (solicitud_id, nombre, apellidos, edad, provincia_residente, telefono, discapacidad, seguridad_social, soltero_o_viudo, vive_en_residencia, viajara_con_acompanante, imserso_anopasado, imserso_2021, importe_pension, porcentaje_discapacidad)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        try:
            cursor.execute(insert_query, (
                datos['solicitud_id'],
                datos['nombre'],
                datos['apellidos'],
                datos['edad'],
                datos['provincia_residente'],
                datos['telefono'],
                datos['discapacidad'],
                datos['seguridad_social'],
                datos['soltero_o_viudo'],
                datos['vive_en_residencia'],
                datos['viajara_con_acompanante'],
                datos['imserso_anopasado'],
                datos['imserso_2021'],
                datos['importe_pension'],
                datos['porcentaje_discapacidad']
            ))
        except Exception as e:
            print(f"Error during insertion: {e}")
            print(f"Failed data: {datos}")

    # Guarda los cambios en la base de datos
    connection.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cierra el cursor y la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
