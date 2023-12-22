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

'''
TABLA SOLICITUDES
'''
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



'''
TABLA TIPO DESTINOS
'''
tipos_todos = []

tipo_insular = {
    'Tipo': 1,
    'Duracion': '8-10 días'
}
tipo_peninsular = {
    'Tipo': 2,
    'Duracion': '8-10 días'
}

tipo_escapada = {
    'Tipo': 3,
    'Duracion': '4-5 días'
}

tipos_todos.append(tipo_insular)
tipos_todos.append(tipo_peninsular)
tipos_todos.append(tipo_escapada)

tipo_destinos_df = pd.DataFrame(tipos_todos)
print(tipo_destinos_df)



'''
TABLA DESTINOS
'''
destinos_todos=[]

costa_peninsular = ['Benidorm', 'Torrevieja', 'Denia', 'Javea', 'El Albir', 'Calpe', 'Peñiscola', 'Benicassim', 'Vinaros', 'Gandia', 'Alboraya', 'Cullera', 'La Manga', 'Roquetas de Mar', 'Mojacar', 'Almuñecar', 'Matalascañas', 'Punta Umbria', 'Torremolinos', 'Marbella', 'Fuengirola', 'Benalmadena', 'Cadiz', 'Calella', 'Pineda del Mar', 'Santa Susana', 'Lloret de Mar', 'Salou', 'Cambrils', 'Comarruga', 'Finestrat', 'Altea', 'Elche', 'Murcia', 'Los Urrutias', 'Aguadulce', 'Isla Antilla', 'Isla Cristina', 'Isla Canela', 'Estepona', 'Conil De La Frontera', 'Chiclana De La Frontera', 'Puerto De Santa María', 'Chipiona', 'Mataro', 'Malgrat De Mar', 'Tossa De Mar', 'Platja D\'Aro', 'San Carlos de la Rapita', 'La Pineda-Vilaseca', 'Miami Platja']

costa_insular = ['Puerto de Alcudia', 'Playa de Muro', 'Palmanova', 'El Arenal', 'Magaluf', 'Cala Rajada', 'Mercadal', 'Ciudadela', 'Punta Prima', 'Santa Eulalia', 'Es Canar', 'San Antonio', 'San Carlos', 'Santa Eulalia', 'Puerto Rico', 'Las Palmas D.G.C.', 'Playa Del Inglés', 'Maspalomas', 'Costa Teguise', 'Puerto de la Cruz', 'Las Caletillas', 'Los Realejos', 'San Miguel De Abona', 'Costa Calma', 'Caleta De Fuste', 'Pajara', 'Fuerteventura']

escapada = ['Finestrat', 'Madrid', 'San Lorenzo del Escorial', 'Pinto', 'Aranjuez', 'Huesca', 'Teruel', 'Zaragoza', 'Oviedo', 'Gijon', 'Agua Dulce', 'San Carlos de la Repita', 'Cabuerniga', 'Ciudad Real', 'Cuenca', 'Guadalajara', 'Toledo', 'Albacete', 'Avila', 'Burgos', 'Zamora', 'Soria', 'Segovia', 'Salamanca', 'Leon', 'Valladolid', 'Palencia', 'Suances', 'Torre La Vega', 'Santander', 'Santoña', 'Can Pastilla', 'Las Palmas D.G.C.', 'Almería', 'Granada', 'Mijas', 'Jerez', 'Jaén', 'Córdoba', 'Sevilla', 'Barcelona', 'Girona', 'Tarragona', 'Reus', 'Alicante', 'Valencia', 'Murcia', 'Talavera De La Reina', 'Zamora', 'Soria', 'Segovia', 'León', 'Valladolid', 'Palencia', 'Salamanca', 'Cáceres', 'Badajoz', 'Mérida', 'Orense', 'La Coruña', 'Lugo', 'Santiago De Compostela', 'Pamplona', 'San Sebastián', 'Bilbao', 'Eibar', 'Ceuta', 'Haro']

for destino in costa_insular:
    datos = {
        'Destino': destino,
        'Tipo de destino': 1
    }
    destinos_todos.append(datos)

for destino in costa_peninsular:
    datos = {
        'Destino': destino,
        'Tipo de destino': 2
    }
    destinos_todos.append(datos)

for destino in escapada:
    datos = {
        'Destino': destino,
        'Tipo de destino': 3
    }
    destinos_todos.append(datos)

destinos_df = pd.DataFrame(destinos_todos)
destinos_df['indice'] = destinos_df.index
print(destinos_df)


'''
TABLA HOTELES
'''
hoteles =['Alua Bocaccio','Aluasun Continental Park','Aluason Torrenova','Caribbean Bay','Habana Bay','Linda','Mediterranean Bay','Palma Bay',
    'Ritort','Samos','Atlantic Park','Triton beach','Linda','Mll Mediterranean Bay Adults Only','Aguamarina I','Aguamarina II',
    'Cala Galdana','Sur Menorca','Almirante Ferragut','Atlantic','Coral Beach','Ereso','Es Pla','San Antonio','Invisa Figueral Resort','Invisa La Cala',
    'Altamadores','Altamar','Concorde','Occidental Las Canteras','Green Field','Koala Garden','Astoria','Blue Sea Costa Teguise Gardens','Alua Parque San Antonio',
    'Alua Tenerife','Aluasoul Orotava Valley','Catalonia Las Vegas','Checkin Concordia Playa','HC Hotel Magec','Marquesa','Parque Vacacional Eden',
    'Valle Orotava','Catalonia Punta del Rey','Panorámica Garden','Barceló Tenerife','Royal Suite','Chatur Costa Caleta','Hotel Royal Suite','Smy Tahona Fuerteventura',
    'Alua Golf Trinidad','Bahía Serena','Best Roquetas','Best Sabinal','El Palmeral','Best Mojacar','Ele Andarax','Portomagno',
    'Vertice Indalo Almeria','Chinasol','Toboso','Checkin Camino De Granada','Dunas de Doñana Golf Resort','Flamero','Gran Hotel del Coto','Pato Amarillo',
    'Ilunion Islantilla','Occidental Isla Cristina','Playacanela','Aluasoul Costa Málaga','Aluasun Costa Park','Marconfort Griego','Parasol Garden',
    'Puente Real','Aluasun Marbella Park','Globales Gardenia','Las Palmeras', 'Medplaya Bali','Medplaya Balmoral','Paraiso Beach','Ilunion Mijas',
    'Ilunion Calas De Conil','Ilunion Sancti Petri','Melia Atlantera','Puerto Sherry','Vertice Chipiona Mar','Nh Avenida Jerez','Condestable Iranzo',
    'Crisol Jardines De Córdoba','Exe Las Adelfas','Castillo','Catalonia Hispalis''Htop Amaika & Spa', 'Htop Calella Palace Family & Spa', 'Santa Mónica',
    'Htop Pineda Palace','Mercury','Ciudad de Mataro','Ibersol Sorra Dor', 'Luna Park Yoga & Spa','Exe Cristal Palace','Garbi Park', 
    'Gran Garbi', 'Htop Royal Star & Spa', 'Samba','Surf-Mar','Tossa Beach Center','Caleta Palace','Platja Park','Best Western P. Cmc Girona',
    'Best Da Vinci', 'Best Los Ángeles', 'Best Mediterráneo', 'Best San Diego', 'Calypso','Htop Molinos Park', 'Medplaya Pirámide Salou','Oasis Park',
    'Best Cambrils','La Rapita','Natura Park','Estival Park Silmar','Medplaya Pino Alto','Ciutat De Tarragona','Gaudi','Dominio de Benidorm con Acapulco', 'Benidorm East',
    'Brasil','Caballo de Oro','Cabana','Carlos I','Cuco','Dynastic' ,'Fiesta Park' ,'Gala Placidia' ,'Golden' ,'Gran Hotel Bali' ,'Jaime I',
    'Joya', 'Lido' ,'Los Álamos' ,'Magic Cristal Park' ,'Magic Rock Gardens' ,'Mareny Benidorm', 'Melina' ,'Mont Park' ,'Montesol' ,'Oasis Plaza', 
    'Olympus' ,'Port Vista Oro' ,'Poseidón Playa' , 'Poseidón Resort', 'Sol y Sombra' ,'Tropic Relax','Alone','Playas Torrevieja','Port Denia',
	'Villa Naranjo','Sun Palace Albir','Port Europa','Roca Esmeralda','Cap Negret' ,'Port Elche' ,'Port Alicante' ,'Aparthotel & Spa Acualandia', 
    'Gran Hotel Peñíscola', 'Aparthotel & Spa Acuazul', 'RH Casablanca Suites' , 'RH Don Carlos & Spa','Intur Orange' ,'RH Vinarós Playa' ,
    'Porto','RH Bayren Park','RH Gijón','Safari','Tres Anclas','Villa Luz','Sicania','Olympia','Port Feria','La Mirage','Aluason Doblemar',
    'Entremares','Izan Cavanna','Occidental Mar Menor','Allegro Murcia Azarbe','Miranda Suizo','Florida','Villa De Pinto','Equo Aranjuez','Axor Feria',
    'Pedro I De Aragon','Rey Sancho Ramírez','Albarracín','Civera','Reina Cristina','Mora','Eurostars Zaragoza','Eurostars Boston',
    'Exe Oviedo Centro','Arbeyal','Arha Villa De Suances','Torresport','Arha Santander','Arha Villa de Santoña','Arha Reserva Del Saja','Nh Ciudad Real',
    'Exe Cuenca', 'Guadalajara & Conference Center','Perales','Be Live City Center Talavera','Eurostars Toledo','Reina Victoria','Cuatro Postes',
    'Puerta De Gredos','Exe Puerta de Burgos','Corona de Castilla','Rey Arturo','Alda Mercado De Zamora','Alfonso Viii Soria','Ele Acueducto',
    'Leon Camino','Olid','Rey Sancho','Gran Hotel Corona Sol','Extremadura Hotel','Ilunion Golf Badajoz','Gran Hotel Corona Sol','Exe Auriense',
    'Exe Coruña','Mendez Nuñez','Ciudad De Compostela','Sancho Ramirez','Barcelo Costa Vasca','Occidental Bilbao','Unzaga Plaza','Ceuta Puerta De Africa','Ciudad De Haro'
]
print(len(hoteles))
lista_ciudades = [
    'Puerto de Alcudia', 'Playa de Muro', 'Palmanova', 'El Arenal', 'El Arenal', 'El Arenal', 'El Arenal', 'El Arenal',
    'Magaluf', 'Magaluf', 'Cala Rajada', 'Can Pastilla', 'El Arenal', 'Mercadal', 'Mercadal', 'Ciudadela', 'Punta Prima', 'Ciudadela',
    'Santa Eulalia', 'Es Canar', 'Es Canar', 'San Antonio', 'San Carlos', 'Santa Eulalia', 'Puerto Rico', 'Puerto Rico',
    'Las Palmas D.G.C.', 'Las Palmas D.G.C.', 'Playa Del Inglés', 'Maspalomas', 'Las Palmas D.G.C.', 'Costa Teguise',
    'Puerto de la Cruz', 'Puerto de la Cruz', 'Puerto de la Cruz', 'Puerto de la Cruz', 'Puerto de la Cruz',
    'Puerto de la Cruz', 'Puerto de la Cruz', 'Puerto de la Cruz', 'Puerto de la Cruz', 'Las Caletillas', 'Los Realejos',
    'San Miguel De Abona', 'Costa Calma', 'Caleta De Fuste', 'Pajara', 'Fuerteventura', 'Roquetas del Mar',
    'Roquetas del Mar', 'Roquetas del Mar', 'Roquetas del Mar', 'Roquetas del Mar', 'Mojacar', 'Aguadulce', 'Aguadulce',
    'Almeria', 'Almuñécar', 'Almuñécar', 'Granada', 'Matalascañas', 'Matalascañas', 'Matalascañas', 'Punta Umbría',
    'Isla Antilla', 'Isla Cristina', 'Isla Canela', 'Torremolinos', 'Torremolinos', 'Torremolinos', 'Torremolinos',
    'Torremolinos', 'Marbella', 'Fuengirola', 'Fuengirola', 'Benalmádena', 'Benalmádena', 'Estepona', 'Mijas',
    'Conil De La Frontera', 'Chiclana De La Frontera', 'Cadiz', 'Puerto De Santa María', 'Chipiona', 'Jerez', 'Jaén',
    'Córdoba', 'Córdoba', 'Córdoba', 'Sevilla', 'Calella', 'Calella', 'Calella', 'Pineda del Mar', 'Santa Susana',
    'Mataro', 'Malgrat De Mar', 'Malgrat De Mar', 'Barcelona', 'Lloret del Mar', 'Lloret del Mar', 'Lloret del Mar',
    'Lloret del Mar', 'Lloret del Mar','Tossa De Mar', 'Platja DAro', 'Platja DAro', 'Girona', 'Salou', 'Salou', 'Salou', 'Salou',
    'Salou', 'Salou', 'Salou', 'Salou', 'Cambrils', 'San Carlos de la Rapita', 'Comarruga', 'La Pineda-Vilaseca',
    'Miami Platja', 'Tarragona', 'Reus', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm',
    'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm',
    'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm',
    'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm',
    'Finestrat', 'Torrevieja', 'Denia', 'Jávea', 'El Albir', 'Calpe', 'Calpe',
    'Altea', 'Elche', 'Alicante', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Benicassim',
    'Vinaros', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Cullera', 'Alboraya', 'Valencia', 'Murcia', 'La Manga',
    'La Manga', 'La Manga', 'Los Urrutias', 'Murcia', 'San Lorenzo del Escorial', 'San Lorenzo del Escorial', 'Pinto',
    'Aranjuez', 'Madrid', 'Huesca', 'Huesca', 'Teruel', 'Teruel', 'Teruel', 'Teruel', 'Zaragoza', 'Zaragoza',
    'Oviedo', 'Gijón', 'Suances', 'Torrelavega', 'Santander', 'Santoña', 'Cabuérniga', 'Ciudad Real', 'Cuenca',
    'Guadalajara', 'Toledo', 'Toledo', 'Toledo', 'Talavera De La Reina', 'Albacete', 'Ávila', 'Ávila', 'Burgos',
    'Burgos', 'Burgos', 'Zamora', 'Soria', 'Segovia', 'León', 'Valladolid', 'Palencia', 'Salamanca', 'Cáceres',
    'Badajoz', 'Mérida', 'Orense', 'La Coruña', 'Lugo', 'Santiago De Compostela', 'Pamplona', 'San Sebastián',
    'Bilbao', 'Eibar', 'Ceuta', 'Haro'
]

hoteles_df = pd.DataFrame()
hoteles_df['Nombres'] = hoteles
hoteles_df['Ciudades'] = lista_ciudades
hoteles_df['indice'] = hoteles_df.index

print(hoteles_df)



'''
TABLA PREFERENCIAS
'''
# Crear una lista de 1000 personas con índices y destinos aleatorios
personas = []
for i in range(1, 1001):
    opcion1 = random.choice(destinos_df['Destino'])
    opcion2 = random.choice(destinos_df['Destino'])
    opcion3 = random.choice(destinos_df['Destino'])
    opcion4 = random.choice(destinos_df['Destino'])
    opcion5 = random.choice(destinos_df['Destino'])
    
    personas.append([i, opcion1, opcion2, opcion3, opcion4, opcion5])

# Crear un DataFrame con la lista de personas
columnas = ['índice', 'Opcion1', 'Opcion2', 'Opcion3', 'Opcion4', 'Opcion5']
preferencias_df = pd.DataFrame(personas, columns=columnas)



