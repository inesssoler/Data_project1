import json

with open('/pgadmin-config.json', 'r') as config_file:
    config = json.load(config_file)

server_data = config['Servers']['1']

# Crear un script SQL con comandos de configuración
script_content = ""
for server_id, server_config in server_data.items():
    script_content += f"""
        -- Configuración para el servidor {server_config.get('Name')}
        INSERT INTO public.servers (servergroup_id, name, host, port, maintenance_db, username, password, ssl_mode)
        VALUES (
            (SELECT id FROM public.servergroups WHERE name = '{server_config.get('Group')}'),
            '{server_config.get('Name')}',
            '{server_config.get('Host')}',
            {server_config.get('Port')},
            '{server_config.get('MaintenanceDB')}',
            '{server_config.get('Username')}',
            '{server_config.get('Password')}',
            '{server_config.get('SSLMode')}'
        );
    """

with open('/docker-entrypoint-initdb.d/pgadmin-setup.sql', 'w') as script_file:
    script_file.write(script_content)


   