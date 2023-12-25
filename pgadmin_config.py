import os

DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')

# Configuración de la aplicación PgAdmin
DEFAULT_SERVER = 'DBImserso'
DEFAULT_SERVER_PORT = 5050
DEFAULT_SERVER_MODE = True
