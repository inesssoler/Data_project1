import json
import random
from faker import Faker

fake = Faker('es_ES')

num_registros = 1000

base_de_datos = []

for _ in range(num_registros):
    datos = {
        'nombre': fake.name(),
        'apellidos': fake.last_name(),
        'edad': random.randint(60, 99),
        'direccion': fake.address(),
        'email': fake.email(),
        'telefono': fake.phone_number(),
        'discapacitado': fake.boolean(),
        'numero_seguridad_social': fake.ssn()
    }
    base_de_datos.append(datos)
    base_de_datos.append(datos)

# Guardar la base de datos en un archivo JSON
with open('base_de_datos.json', 'w') as archivo:
    json.dump(base_de_datos, archivo, indent=2)

print("Base de datos generada y guardada en 'base_de_datos.json'")