import pandas as pd
import random

# TABLA DESTINOS

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



# Lista de ciudades desde destinos_df
destinos_df = pd.DataFrame(destinos_todos)
destinos_df['indice'] = destinos_df.index

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
df_preferencias = pd.DataFrame(personas, columns=columnas)
