import pandas as pd
import numpy as np
import random
import json
from faker import Faker

fake = Faker('es_ES')

num_registros = 10000
base_de_datos = []

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
        'accesotransp': fake.boolean(),
        'imserso_anopasado': fake.boolean(),  
        'imserso_2021': fake.boolean(),  
        'importe_pension': round(random.uniform(480, 3000))
    }

    if datos['discapacidad']:
       datos['porcentaje_discapacidad'] = round(random.uniform(1, 85))
    else:
       datos['porcentaje_discapacidad'] = 0

    base_de_datos.append(datos)

df = pd.DataFrame(base_de_datos)

df.to_csv('base_de_datos.csv', index=False, encoding='utf-8')  # Guardar en formato CSV

print("Base de datos generada y guardada en 'base_de_datos.csv'")

# Carga los datos desde el CSV
personas = pd.read_csv('base_de_datos.csv')

def calcular_puntaje(datos):
    puntaje = 0

    # Puntaje según la edad
    if 65 <= datos['edad'] <= 75:
        puntaje += 10
    elif 76 <= datos['edad'] <= 85:
        puntaje += 15
    elif datos['edad'] > 86:
        puntaje += 20

    # Puntaje por estado civil
    puntaje += 10 if datos['soltero_o_viudo'] else 0

    # Puntaje por si vive en residencia de mayores
    puntaje += 15 if datos['vive_en_residencia'] else 0

    # Puntaje por discapacidad
    if 30 <= datos['discapacidad'] <= 41:
        puntaje += 5
    elif 42 <= datos['discapacidad'] <= 53:
        puntaje += 10
    elif 54 <= datos['discapacidad'] <= 65:
        puntaje += 15
    elif 66 <= datos['discapacidad'] <= 77:
        puntaje += 20
    elif datos['discapacidad'] > 78:
        puntaje += 25

    # Puntaje por acceso a transporte
    puntaje += 1 if datos['accesotransp'] else 5

    # Puntaje por provincia
    provincias_puntajes = {
        'Alicante': 1,
        'Castellón': 1,
        'Valencia': 1,
        'Murcia': 1,
        'Almería': 1,
        'Granada': 1,
        'Huelva': 1,
        'Sevilla': 1,
        'Córdoba': 1,
        'Jaén': 1,
        'Málaga': 1,
        'Cádiz': 1,
        'Girona': 2,
        'Barcelona': 2,
        'Tarragona': 2,
        'Lleida': 2,
        'Ourense': 2,
        'Lugo': 2,
        'Pontevedra': 2,
        'A Coruña': 2,
        'Asturias': 2,
        'Bilbao': 2,
        'Álava': 2,
        'Vizcaya': 2,
        'Guipúzcoa': 2,
        'Albacete': 3,
        'Ciudad Real': 3,
        'Cuenca': 3,
        'Guadalajara': 3,
        'Toledo': 3,
        'Badajoz': 3,
        'Cáceres': 3,
        'Madrid': 4,
        'Huesca': 5,
        'Zaragoza': 5,
        'Teruel': 5,
        'La Rioja': 5,
        'Navarra': 5,
        'Pamplona': 5,
        'Cantabria': 5,
        'Burgos': 6,
        'León': 6,
        'Palencia': 6,
        'Zamora': 6,
        'Valladolid': 6,
        'Soria': 6,
        'Segovia': 6,
        'Ávila': 6,
        'Salamanca': 6,
        'Baleares': 7,
        'Las Palmas': 7,
        'Santa Cruz de Tenerife': 7,
        'Ceuta': 7,
        'Melilla': 7
    }
    puntaje += provincias_puntajes.get(datos['provincia_residente'].lower(), 0)

    # Puntaje por año de viaje
    if datos['imserso_anopasado'] and datos['imserso_2021']:
            puntaje += 1
    elif datos['imserso_anopasado'] and not datos['imserso_2021']:
            puntaje += 5
    elif not datos['imserso_anopasado'] and datos['imserso_2021']:
            puntaje += 10
    else:
            puntaje += 25

    # Puntaje por pensión
    if 480 <= datos['importe_pension'] <= 996:
        puntaje += 35
    elif 997 <= datos['importe_pension'] <= 1513:
        puntaje += 20
    elif 1514 <= datos['importe_pension'] <= 2030:
        puntaje += 10
    elif 2031 <= datos['importe_pension'] <= 2547:
        puntaje += 5
    elif datos['importe_pension'] > 2548:
        puntaje += 1

    return puntaje

# Aplica la función "calcular_puntaje" a cada fila del DataFrame y agrega los resultados a una nueva columna llamada 'puntaje'
personas['puntaje'] = personas.apply(calcular_puntaje, axis=1)

# Muestra el DF con la columna 'puntaje'
print(personas[['nombre', 'puntaje']])
# Tabla de destinos
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

# Carga los hoteles y destinos con sus plazas correspondientes
hoteles = ['Alua Bocaccio','Aluasun Continental Park','Aluason Torrenova','Caribbean Bay','Habana Bay','Linda','Mediterranean Bay','Palma Bay',
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
    'Exe Coruña','Mendez Nuñez','Ciudad De Compostela','Sancho Ramirez','Barcelo Costa Vasca','Occidental Bilbao','Unzaga Plaza','Ceuta Puerta De Africa','Ciudad De Haro']

lista_ciudades = ['Puerto de Alcudia', 'Playa de Muro', 'Palmanova', 'El Arenal', 'El Arenal', 'El Arenal', 'El Arenal', 'El Arenal',
    'El Arenal', 'Magaluf', 'Cala Rajada', 'Can Pastilla', 'El Arenal', 'Mercadal', 'Mercadal', 'Ciudadela', 'Punta Prima', 'Ciudadela',
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
    'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Benidorm', 'Finestrat', 'Torrevieja', 'Denia', 'Jávea', 'El Albir', 'Calpe', 'Calpe',
    'Altea', 'Elche', 'Alicante', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Peñíscola', 'Benicassim',
    'Vinaros', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Gandía', 'Cullera', 'Alboraya', 'Valencia', 'Murcia', 'La Manga',
    'La Manga', 'La Manga', 'Los Urrutias', 'Murcia', 'San Lorenzo del Escorial', 'San Lorenzo del Escorial', 'Pinto',
    'Aranjuez', 'Madrid', 'Huesca', 'Huesca', 'Teruel', 'Teruel', 'Teruel', 'Teruel', 'Zaragoza', 'Zaragoza',
    'Oviedo', 'Gijón', 'Suances', 'Torrelavega', 'Santander', 'Santoña', 'Cabuérniga', 'Ciudad Real', 'Cuenca',
    'Guadalajara', 'Toledo', 'Toledo', 'Toledo', 'Talavera De La Reina', 'Albacete', 'Ávila', 'Ávila', 'Burgos',
    'Burgos', 'Burgos', 'Zamora', 'Soria', 'Segovia', 'León', 'Valladolid', 'Palencia', 'Salamanca', 'Cáceres',
    'Badajoz', 'Mérida', 'Orense', 'La Coruña', 'Lugo', 'Santiago De Compostela', 'Pamplona', 'San Sebastián',
    'Bilbao', 'Eibar', 'Ceuta', 'Haro']

hoteles_df = pd.DataFrame()
hoteles_df['Nombres'] = hoteles
hoteles_df['Ciudades'] = lista_ciudades
hoteles_df['indice'] = hoteles_df.index
hoteles_df['Plazas'] = [random.randint(130, 220)
    for _ in range(len(hoteles_df))]

total_plazas_por_provincia = hoteles_df.groupby('Ciudades')['Plazas'].sum().reset_index()
print(total_plazas_por_provincia)

print(hoteles_df)

# Obtiene una lista única de ciudades
ciudades_unicas = list(set(lista_ciudades))

def obtener_preferencias_viaje(datos):
    # Selecciona 5 ciudades aleatorias sin repetir como preferencias y las asigna a cada viajero
    preferencias = random.sample(ciudades_unicas, min(5, len(ciudades_unicas)))
    return preferencias

personas['preferencias_viajes'] = personas.apply(obtener_preferencias_viaje, axis=1)

print(personas[['nombre', 'preferencias_viajes']])

def asignar_hoteles(personas, hoteles_df, primer_recorrido=True, asignaciones_previas=None):
    # Establece asignaciones como una lista vacía
    asignaciones = []

    # Crea la variable para realizar un seguimiento de la ciudad asignada en el primer recorrido
    ciudad_asignada_primer_recorrido = None

    # Si hay asignaciones previas del primer recorrido, excluiye las preferencias en la segunda ronda
    if asignaciones_previas is not None:
        preferencias_excluidas = asignaciones_previas['preferencias_asignadas'].explode().unique()

    # Ordena las personas por puntaje de mayor a menor
    personas = personas.sort_values(by=['puntaje'], ascending=False)

    for index, persona in personas.iterrows():
        # Obtiene las preferencias del viajero
        preferencias = persona['preferencias_viajes']

        # En el segundo recorrido, excluye la ciudad asignada en el primer recorrido para que no viaje dos veces al mismo destino
        if not primer_recorrido and ciudad_asignada_primer_recorrido is not None:
            preferencias = [preferencia for preferencia in preferencias if preferencia != ciudad_asignada_primer_recorrido]

        hoteles_asignados = []

        for preferencia in preferencias:
            # Filtra los hoteles disponibles en la ciudad de preferencia
            hoteles_disponibles = hoteles_df[(hoteles_df['Ciudades'] == preferencia) & (hoteles_df['Plazas'] > 0)]

            # Excluye los hoteles que ya le han sido asignados a ese viajero
            hoteles_disponibles = hoteles_disponibles[~hoteles_disponibles['Nombres'].isin(hoteles_asignados)]

            for _ in range(2):  # Intenta asignar hasta un máximo de dos hoteles
                if not hoteles_disponibles.empty and len(hoteles_asignados) < 2:
                    # Selecciona el hotel con más plazas disponibles y lo asigna según el puntaje obtenido
                    hotel_asignado = hoteles_disponibles.loc[hoteles_disponibles['Plazas'].idxmax()]

                    # Actualiza las plazas disponibles del hotel y su ciudad
                    plazas_a_restar = 2 if persona['viajara_con_acompanante'] else 1
                    hoteles_df.loc[hoteles_df['indice'] == hotel_asignado['indice'], 'Plazas'] -= plazas_a_restar

                    # Almacena la asignación en la lista de hoteles asignados
                    hoteles_asignados.append(hotel_asignado['Nombres'])

                    # Elimina el hotel asignado de la lista de disponibles en caso de no quedar plazas
                    hoteles_disponibles = hoteles_disponibles[~(hoteles_disponibles['indice'] == hotel_asignado['indice'])]

                    # En el primer recorrido, almacena la ciudad asignada
                    if primer_recorrido:
                        ciudad_asignada_primer_recorrido = preferencia

                else:
                    break  # Sale si no hay más hoteles disponibles para asignar

        # Almacena la información de asignaciones en el formato correspondiente
        asignacion = {'nombre': persona['nombre'], 'hoteles_asignados': hoteles_asignados, 'preferencias_asignadas': preferencias}
        asignaciones.append(asignacion)

    # Convierte la lista de asignaciones a un DF
    asignaciones_df = pd.DataFrame(asignaciones)

    # Si es el primer recorrido y ya se le asignó un hotel, realizar un segundo recorrido
    if primer_recorrido and not asignaciones_df['hoteles_asignados'].apply(lambda x: len(x)).eq(0).all():
        # Realiza una copia de los DFs para evitar problemas de referencia
        personas_copia = personas.copy(deep=True)
        hoteles_df_copia = hoteles_df.copy(deep=True)

        # Llama de forma indefinida a la función para un segundo recorrido
        asignaciones_df_adicional = asignar_hoteles(personas_copia, hoteles_df_copia, primer_recorrido=False, asignaciones_previas=asignaciones_df)

        # Combina las asignaciones adicionales con las existentes
        asignaciones_df = pd.concat([asignaciones_df, asignaciones_df_adicional], ignore_index=True)

    return asignaciones_df

# Llama a la función "asignar_hoteles"
asignaciones = asignar_hoteles(personas, hoteles_df)

# Muestra el DF con las asignaciones finales
print('--------------------------------------------------Asignaciones--------------------------------------------------\n')
print(asignaciones)
asignaciones.to_csv('asignaciones.csv', index=False, encoding='utf-8')