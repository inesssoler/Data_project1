import pandas as pd

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