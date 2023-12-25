import os
from pgadmin4 import create_app

# Configuración del servidor PgAdmin
PGADMIN_CONFIG = os.path.join(os.path.dirname(__file__), 'pgadmin_config.py')
PGADMIN_APP = create_app(config_file=PGADMIN_CONFIG)

 # Inicia el servidor PgAdmin
PGADMIN_APP.run()

