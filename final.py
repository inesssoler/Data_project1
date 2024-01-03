import pandas as pd
import numpy as np
import random
import json
import psycopg2
from faker import Faker
from sqlalchemy import create_engine

# Conexión a la base de datos
connection_params = {
    'dbname': "data_project1",
    'user': 'postgres',
    'password': 'Welcome01',
    'host': 'localhost',
    'port': '5432'
}

engine = create_engine('postgresql+psycopg2://postgres:Welcome01@localhost:5432/data_project1')

solicitudes_df = pd.read_sql('SELECT * FROM solicitudes', con=engine)
ciudades_df = pd.read_sql('SELECT * FROM ciudades', con=engine)
preferencias_df = pd.read_sql('SELECT * FROM preferencias', con=engine)
destino_df = pd.read_sql('SELECT * FROM destinos', con=engine)
hoteles_df = pd.read_sql('SELECT * FROM hoteles', con=engine)
print(preferencias_df.columns)

print('Bien')

# Crear un diccionario de mapeo entre ciudades y tipos
tipo_destino_mapping = {}

costa_peninsular = ['Benidorm', 'Torrevieja', 'Denia', 'Javea', 'El Albir', 'Calpe', 'Peñiscola', 'Benicassim', 'Vinaros', 'Gandia', 'Alboraya', 'Cullera', 'La Manga', 'Roquetas de Mar', 'Mojacar', 'Almuñecar', 'Matalascañas', 'Punta Umbria', 'Torremolinos', 'Marbella', 'Fuengirola', 'Benalmadena', 'Cadiz', 'Calella', 'Pineda del Mar', 'Santa Susana', 'Lloret de Mar', 'Salou', 'Cambrils', 'Comarruga', 'Finestrat', 'Altea', 'Elche', 'Murcia', 'Los Urrutias', 'Aguadulce', 'Isla Antilla', 'Isla Cristina', 'Isla Canela', 'Estepona', 'Conil De La Frontera', 'Chiclana De La Frontera', 'Puerto De Santa María', 'Chipiona', 'Mataro', 'Malgrat De Mar', 'Tossa De Mar', 'Platja D\'Aro', 'San Carlos de la Rapita', 'La Pineda-Vilaseca', 'Miami Platja']
costa_insular = ['Puerto de Alcudia', 'Playa de Muro', 'Palmanova', 'El Arenal', 'Magaluf', 'Cala Rajada', 'Mercadal', 'Ciudadela', 'Punta Prima', 'Santa Eulalia', 'Es Canar', 'San Antonio', 'San Carlos', 'Santa Eulalia', 'Puerto Rico', 'Las Palmas D.G.C.', 'Playa Del Inglés', 'Maspalomas', 'Costa Teguise', 'Puerto de la Cruz', 'Las Caletillas', 'Los Realejos', 'San Miguel De Abona', 'Costa Calma', 'Caleta De Fuste', 'Pajara', 'Fuerteventura']
escapada = ['Finestrat', 'Madrid', 'San Lorenzo del Escorial', 'Pinto', 'Aranjuez', 'Huesca', 'Teruel', 'Zaragoza', 'Oviedo', 'Gijon', 'Agua Dulce', 'San Carlos de la Repita', 'Cabuerniga', 'Ciudad Real', 'Cuenca', 'Guadalajara', 'Toledo', 'Albacete', 'Avila', 'Burgos', 'Zamora', 'Soria', 'Segovia', 'Salamanca', 'Leon', 'Valladolid', 'Palencia', 'Suances', 'Torre La Vega', 'Santander', 'Santoña', 'Can Pastilla', 'Las Palmas D.G.C.', 'Almería', 'Granada', 'Mijas', 'Jerez', 'Jaén', 'Córdoba', 'Sevilla', 'Barcelona', 'Girona', 'Tarragona', 'Reus', 'Alicante', 'Valencia', 'Murcia', 'Talavera De La Reina', 'Zamora', 'Soria', 'Segovia', 'León', 'Valladolid', 'Palencia', 'Salamanca', 'Cáceres', 'Badajoz', 'Mérida', 'Orense', 'La Coruña', 'Lugo', 'Santiago De Compostela', 'Pamplona', 'San Sebastián', 'Bilbao', 'Eibar', 'Ceuta', 'Haro']

for destino in costa_peninsular:
    tipo_destino_mapping[destino] = '1'

for destino in costa_insular:
    tipo_destino_mapping[destino] = '2'

for destino in escapada:
    tipo_destino_mapping[destino] = '3'

# Crear una nueva columna 'tipo_destino' en preferencias_df
preferencias_df['tipo_destino'] = preferencias_df['ciudad'].map(tipo_destino_mapping)

# Mostrar las nuevas columnas de tipos en preferencias_df
columnas_tipo_destino = ['ciudad', 'tipo_destino']
tipos_destino_df = preferencias_df[columnas_tipo_destino]
print(tipos_destino_df)

# Obtener las preferencias de la persona
preferencias_persona = preferencias_df[preferencias_df['solicitud_id'] == solicitudes_df['solicitud_id']]
def calcular_puntaje(solicitudes_df, preferencias_persona):
    puntaje = 0
    
    provincias_puntajes_1 = {
        'alicante': 2,
        'castellón': 2,
        'valencia': 2,
        'murcia': 2,
        'almería': 2,
        'granada': 2,
        'huelva': 2,
        'sevilla': 2,
        'córdoba': 2,
        'jaén': 2,
        'málaga': 2,
        'cádiz': 2,
        'girona': 2,
        'barcelona': 2,
        'tarragona': 2,
        'lleida': 2,
        'ourense': 3,
        'lugo': 3,
        'pontevedra': 3,
        'a coruña': 3,
        'asturias': 3,
        'bilbao': 3,
        'álava': 3,
        'vizcaya': 3,
        'guipúzcoa': 3,
        'albacete': 3,
        'ciudad real': 3,
        'cuenca': 3,
        'guadalajara': 3,
        'toledo': 3,
        'badajoz': 3,
        'cáceres': 3,
        'madrid': 3,
        'huesca': 3,
        'zaragoza': 3,
        'teruel': 3,
        'la rioja': 3,
        'navarra': 3,
        'pamplona': 3,
        'cantabria': 3,
        'burgos': 3,
        'león': 3,
        'palencia': 3,
        'zamora': 3,
        'valladolid': 3,
        'soria': 3,
        'segovia': 3,
        'ávila': 3,
        'salamanca': 3,
        'baleares': 1,
        'las palmas': 1,
        'santa cruz de tenerife': 1,
        'ceuta': 1,
        'melilla': 1
    }
    provincias_puntajes_2 = {
        'alicante': 1,
        'castellón': 1,
        'valencia': 1,
        'murcia': 1,
        'almería': 1,
        'granada': 1,
        'huelva': 1,
        'sevilla': 1,
        'córdoba': 1,
        'jaén': 1,
        'málaga': 1,
        'cádiz': 1,
        'girona': 2,
        'barcelona': 2,
        'tarragona': 2,
        'lleida': 2,
        'ourense': 2,
        'lugo': 2,
        'pontevedra': 2,
        'a coruña': 2,
        'asturias': 2,
        'bilbao': 2,
        'álava': 2,
        'vizcaya': 2,
        'guipúzcoa': 2,
        'albacete': 3,
        'ciudad real': 3,
        'cuenca': 3,
        'guadalajara': 3,
        'toledo': 3,
        'badajoz': 3,
        'cáceres': 3,
        'madrid': 4,
        'huesca': 5,
        'zaragoza': 5,
        'teruel': 5,
        'la rioja': 5,
        'navarra': 5,
        'pamplona': 5,
        'cantabria': 5,
        'burgos': 6,
        'león': 6,
        'palencia': 6,
        'zamora': 6,
        'valladolid': 6,
        'soria': 6,
        'segovia': 6,
        'ávila': 6,
        'salamanca': 6,
        'baleares': 7,
        'las palmas': 7,
        'santa cruz de tenerife': 7,
        'ceuta': 7,
        'melilla': 7
    }
    provincias_puntajes_3 = {
        'alicante': 6,
        'castellón': 6,
        'valencia': 6,
        'murcia': 6,
        'almería': 6,
        'granada': 6,
        'huelva': 6,
        'sevilla': 6,
        'córdoba': 6,
        'jaén': 6,
        'málaga': 6,
        'cádiz': 6,
        'girona': 5,
        'barcelona': 5,
        'tarragona': 5,
        'lleida': 5,
        'ourense': 5,
        'lugo': 5,
        'pontevedra': 5,
        'a coruña': 5,
        'asturias': 5,
        'bilbao': 5,
        'álava': 5,
        'vizcaya': 5,
        'guipúzcoa': 5,
        'albacete': 4,
        'ciudad real': 4,
        'cuenca': 4,
        'guadalajara': 4,
        'toledo': 4,
        'badajoz': 4,
        'cáceres': 4,
        'madrid': 3,
        'huesca': 3,
        'zaragoza': 3,
        'teruel': 3,
        'la rioja': 3,
        'navarra': 3,
        'pamplona': 3,
        'cantabria': 3,
        'burgos': 2,
        'león': 2,
        'palencia': 2,
        'zamora': 2,
        'valladolid': 2,
        'soria': 2,
        'segovia': 2,
        'ávila': 2,
        'salamanca': 2,
        'baleares': 7,
        'las palmas': 7,
        'santa cruz de tenerife': 7,
        'ceuta': 7,
        'melilla': 7
    }
    
    for _, preferencia in preferencias_persona.iterrows():
        tipo_destino = preferencia['tipo_destino']
        
        if tipo_destino == 'costa_insular':
            puntaje += provincias_puntajes_1.get(solicitudes_df['provincia_residente'].iloc[0].lower(), 0)
        elif tipo_destino == 'costa_peninsular':
            puntaje += provincias_puntajes_2.get(solicitudes_df['provincia_residente'].iloc[0].lower(), 0)
        elif tipo_destino == 'escapada':
            puntaje += provincias_puntajes_3.get(solicitudes_df['provincia_residente'].iloc[0].lower(), 0)

    # Puntaje según la edad
    if 65 <= solicitudes_df['edad'].iloc[0] <= 75:
        puntaje += 10
    elif 76 <= solicitudes_df['edad'].iloc[0] <= 85:
        puntaje += 15
    elif solicitudes_df['edad'].iloc[0] > 86:
        puntaje += 20

    # Puntaje por estado civil
    puntaje += 10 if solicitudes_df['soltero_o_viudo'].iloc[0] else 0

    # Puntaje por residencia en mayores
    puntaje += 15 if solicitudes_df['vive_en_residencia'].iloc[0] else 0

    # Puntaje por discapacidad
    if 30 <= solicitudes_df['discapacidad'].iloc[0] <= 41:
        puntaje += 5
    elif 42 <= solicitudes_df['discapacidad'].iloc[0] <= 53:
        puntaje += 10
    elif 54 <= solicitudes_df['discapacidad'].iloc[0] <= 65:
        puntaje += 15
    elif 66 <= solicitudes_df['discapacidad'].iloc[0] <= 77:
        puntaje += 20
    elif solicitudes_df['discapacidad'].iloc[0] > 78:
        puntaje += 25

    # Puntaje por acceso al transporte
    puntaje += 1 if solicitudes_df['acceso_transporte'].iloc[0] else 5

    # Puntaje por año de viaje
    if solicitudes_df['imserso_anopasado'].iloc[0] and solicitudes_df['imserso_2021'].iloc[0]:
        puntaje += 1
    elif solicitudes_df['imserso_anopasado'].iloc[0] and not solicitudes_df['imserso_2021'].iloc[0]:
        puntaje += 5
    elif not solicitudes_df['imserso_anopasado'].iloc[0] and solicitudes_df['imserso_2021'].iloc[0]:
        puntaje += 10
    else:
        puntaje += 25

    # Puntaje por pensión
    if 480 <= solicitudes_df['importe_pension'].iloc[0] <= 996:
        puntaje += 35
    elif 997 <= solicitudes_df['importe_pension'].iloc[0] <= 1513:
        puntaje += 20
    elif 1514 <= solicitudes_df['importe_pension'].iloc[0] <= 2030:
        puntaje += 10
    elif 2031 <= solicitudes_df['importe_pension'].iloc[0] <= 2547:
        puntaje += 5
    elif solicitudes_df['importe_pension'].iloc[0] > 2548:
        puntaje += 1

    return puntaje

# llamar a la función con los DataFrames correspondientes
puntaje_final = calcular_puntaje(solicitudes_df, preferencias_persona)
print(f"Puntaje final: {puntaje_final}")

# Aplicar la función calcular_puntaje a cada fila del DataFrame y agregar los resultados a una nueva tabla llamada 'puntuaciones'
puntuaciones_df = pd.DataFrame(solicitudes_df[['solicitud_id', 'nombre', 'apellidos']])
puntuaciones_df['puntaje'] = solicitudes_df.apply(calcular_puntaje, axis=1)

# CONEXION E INSERCIÓN DE LOS DATOS A LA TABAL 'PUNTUACIONES'

try:
    connection = psycopg2.connect(
        host="localhost",
        database="data_project1",
        user="postgres",
        password="Welcome01"
    )

    cursor = connection.cursor()

    # Insertar tabla 'puntuaciones'
    for persona in puntuaciones_df.itertuples(index=False):
        insert_puntuaciones_query = """
        INSERT INTO public.puntuaciones 
        (solicitud_id, nombre, apellidos, puntaje)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING;  -- Evita duplicados
        """

        cursor.execute(insert_puntuaciones_query, (
            persona.solicitud_id,
            persona.nombre,
            persona.apellidos,
            persona.puntaje
        ))    


    # Guarda los cambios en la base de datos
    connection.commit()

    puntuaciones_df = pd.read_sql('SELECT * FROM puntuaciones', con=engine)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cierra el cursor y la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()

# Ordenar el DataFrame por la columna 'puntaje'
puntuaciones_df = puntuaciones_df.sort_values(by='puntaje', ascending=False)

total_plazas_por_provincia = hoteles_df.groupby('Ciudades')['Plazas'].sum().reset_index()

def asignar_hoteles(puntuaciones_df, hoteles_df, preferencias_df, primer_recorrido=True):
    # Inicializar asignaciones como una lista vacía
    asignaciones = []
    

    for index, persona in preferencias_df.iterrows():
        # Obtener las preferencias de la persona
        preferencias = persona[['opcion_1', 'opcion_2', 'opcion_3', 'opcion_4', 'opcion_5']]

        hoteles_asignados = []

        for preferencia in preferencias:
            # Filtrar hoteles disponibles en la ciudad de la preferencia
            hoteles_disponibles = hoteles_df[(hoteles_df['ciudad'] == preferencia) & (hoteles_df['plazas'] > 0)]

            # Excluir hoteles que ya han sido asignados a esta persona
            hoteles_disponibles = hoteles_disponibles[~hoteles_disponibles['hotel'].isin(hoteles_asignados)]

            for _ in range(2):  # Intentar asignar hasta dos hoteles
                if not hoteles_disponibles.empty and len(hoteles_asignados) < 2:
                    # Seleccionar el hotel con más plazas disponibles y asignar según el puntaje
                    hotel_asignado = hoteles_disponibles.loc[hoteles_disponibles['plazas'].idxmax()]

                    # Actualizar las plazas disponibles del hotel y ciudad
                    plazas_a_restar = 2 if solicitudes_df['viajara_con_acompanante'].iloc[index] else 1
                    hoteles_df.loc[hoteles_df['hotel_id'] == hotel_asignado['hotel_id'], 'plazas'] -= plazas_a_restar

                    # Almacenar la asignación en la lista de hoteles asignados
                    #if preferencias_df['solicitud_id'] == puntuaciones_df['solicitud_id']:
                    #     nueva_columna = [f'hotel_asignado_{_+1}']
                    #    puntuaciones_df[nueva_columna] = hotel_asignado
                    puntuaciones_df.loc[puntuaciones_df['solicitud_id'] == persona['solicitud_id'], f'hotel_asignado_{_ + 1}'] = hotel_asignado['hotel']


                    # Eliminar el hotel asignado de la lista de disponibles
                    hoteles_disponibles = hoteles_disponibles[~(hoteles_disponibles['hotel_id'] == hotel_asignado['hotel_id'])]

                else:
                    break  # Salir si no hay más hoteles disponibles

    # Si es el primer recorrido, realizar un segundo recorrido
    if primer_recorrido:
        # Realizar una copia profunda de los DataFrames para evitar problemas de referencia
        puntuaciones_df_copia = puntuaciones_df.copy(deep=True)
        hoteles_df_copia = hoteles_df.copy(deep=True)

        # Llamar recursivamente a la función para un segundo recorrido
        asignaciones_df_adicional = asignar_hoteles(puntuaciones_df_copia, hoteles_df_copia, preferencias_df, primer_recorrido=False)

        # Combinar las asignaciones adicionales con las existentes
        puntuaciones_df = pd.concat([puntuaciones_df, asignaciones_df_adicional], ignore_index=True)

    return puntuaciones_df


# Llamar a la función asignar_hoteles
resultado = asignar_hoteles(puntuaciones_df, hoteles_df, preferencias_df)
print(f'Dataframe puntuaciones: {resultado}')
print(f'Dataframe puntuaciones: {puntuaciones_df}')
#print(f'puntuaciones def: {solicitudes_df}')


# CONEXION E INSERCIÓN DE LOS DATOS A LA TABAL 'PUNTUACIONES'

try:
    connection = psycopg2.connect(
        host="localhost",
        database="data_project1",
        user="postgres",
        password="Welcome01"
    )

    cursor = connection.cursor()

    # Insertar tabla 'puntuaciones'
    for persona in puntuaciones_df.itertuples(index=False):
        insert_puntuaciones_query = """
        INSERT INTO public.puntuaciones 
        (hotel_asignado_1, hotel_asignado_2)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;  -- Evita duplicados
        """

        cursor.execute(insert_puntuaciones_query, (
            persona.hotel_asignado_1,
            persona.hotel_asignado_2
        ))    


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

