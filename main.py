from network_analysis import NetworkAnalysis
from report import generate_report
from graph_visualization import draw_social_graph

# Ejemplo de input: puedes modificar estos datos
personas = [
    'Ana', 'Luis', 'Juan', 'Sofía', 'Pedro', 'Marta', 'Carlos', 'Elena', 'Raúl', 'Lucía',
    'Diego', 'Valeria', 'Tomás', 'Paula', 'Andrés'
]
conexiones = [
    ('Ana', 'Luis'), ('Ana', 'Juan'), ('Luis', 'Sofía'), ('Juan', 'Pedro'),
    ('Sofía', 'Pedro'), ('Luis', 'Pedro'), ('Marta', 'Carlos'), ('Carlos', 'Elena'),
    ('Elena', 'Raúl'), ('Raúl', 'Lucía'), ('Lucía', 'Diego'), ('Diego', 'Valeria'),
    ('Valeria', 'Tomás'), ('Tomás', 'Paula'), ('Paula', 'Andrés'), ('Andrés', 'Ana'),
    ('Marta', 'Ana'), ('Carlos', 'Luis'), ('Elena', 'Juan'), ('Raúl', 'Sofía'),
    ('Lucía', 'Pedro'), ('Diego', 'Marta'), ('Valeria', 'Carlos'), ('Tomás', 'Elena'),
    ('Paula', 'Raúl'), ('Andrés', 'Lucía')
]

# Análisis de la red
red = NetworkAnalysis(personas, conexiones)
valores, vectores = red.eigen_analysis()
influencers = red.find_influencers(top_n=3)

# Generar informe
informe = generate_report(personas, influencers, red.adj_matrix, red.laplacian, valores, vectores)

with open('informe.txt', 'w', encoding='utf-8') as f:
    f.write(informe)

print('Informe generado: informe.txt')

# Generar grafo en imagen
salida_imagen = 'grafo.png'
draw_social_graph(personas, conexiones, influencers, filename=salida_imagen)

print(f'Grafo generado: {salida_imagen}')
