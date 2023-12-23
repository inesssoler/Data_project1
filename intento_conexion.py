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