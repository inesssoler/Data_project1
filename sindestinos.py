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


def calcular_puntaje(solicitudes_df):
    puntaje = 0

    # Puntaje según la edad
    if 65 <= solicitudes_df['edad'] <= 75:
        puntaje += 10
    elif 76 <= solicitudes_df['edad'] <= 85:
        puntaje += 15
    elif solicitudes_df['edad'] > 86:
        puntaje += 20

    # Puntaje por estado civil
    puntaje += 10 if solicitudes_df['soltero_o_viudo'] else 0

    # Puntaje por residencia en mayores
    puntaje += 15 if solicitudes_df['vive_en_residencia'] else 0

    # Puntaje por discapacidad
    if 30 <= solicitudes_df['discapacidad'] <= 41:
        puntaje += 5
    elif 42 <= solicitudes_df['discapacidad'] <= 53:
        puntaje += 10
    elif 54 <= solicitudes_df['discapacidad'] <= 65:
        puntaje += 15
    elif 66 <= solicitudes_df['discapacidad'] <= 77:
        puntaje += 20
    elif solicitudes_df['discapacidad'] > 78:
        puntaje += 25

    # Puntaje por acceso al transporte
    puntaje += 1 if solicitudes_df['acceso_transporte'] else 5

    # Puntaje por provincia
    provincias_puntajes = {
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
    puntaje += provincias_puntajes.get(solicitudes_df['provincia_residente'].lower(), 0)


    # Puntaje por año de viaje
    if solicitudes_df['imserso_anopasado'] and solicitudes_df['imserso_2021']:
            puntaje += 1
    elif solicitudes_df['imserso_anopasado'] and not solicitudes_df['imserso_2021']:
            puntaje += 5
    elif not solicitudes_df['imserso_anopasado'] and solicitudes_df['imserso_2021']:
            puntaje += 10
    else:
            puntaje += 25

    # Puntaje por pensión
    if 480 <= solicitudes_df['importe_pension'] <= 996:
        puntaje += 35
    elif 997 <= solicitudes_df['importe_pension'] <= 1513:
        puntaje += 20
    elif 1514 <= solicitudes_df['importe_pension'] <= 2030:
        puntaje += 10
    elif 2031 <= solicitudes_df['importe_pension'] <= 2547:
        puntaje += 5
    elif solicitudes_df['importe_pension'] > 2548:
        puntaje += 1

    return puntaje

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


total_plazas_por_provincia = hoteles_df.groupby('Ciudades')['Plazas'].sum().reset_index()


# Esto ya esta definido en la tabla 'Preferencias'
'''
# Obtener una lista única de ciudades
ciudades_unicas = list(set(lista_ciudades))

def obtener_preferencias_viaje(datos):
    # Seleccionar 5 ciudades aleatorias sin repetir
    preferencias = random.sample(ciudades_unicas, min(5, len(ciudades_unicas)))
    return preferencias

personas['preferencias_viajes'] = personas.apply(obtener_preferencias_viaje, axis=1)

print(personas[['nombre', 'preferencias_viajes']])
'''
# Ordenar el DataFrame por la columna 'puntaje'
puntuaciones_df = puntuaciones_df.sort_values(by='puntaje', ascending=False)


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









