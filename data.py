#------------------------------------------------------------------------------------------------------------------------------------------
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
num_registros = 500

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

# Guarda la base de datos en un JSON con codificación utf-8 y ensure_ascii=False, facilitando las tildes e imprimiéndolo por pantalla
with open('base_de_datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(base_de_datos, archivo, indent=2, ensure_ascii=False)

print("Base de datos generada y guardada en 'base_de_datos.json'")
#------------------------------------------------------------------------------------------------------------------------------------------
