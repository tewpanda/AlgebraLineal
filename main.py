from network_analysis import NetworkAnalysis
from report import generate_report
from graph_visualization import draw_social_graph
import numpy as np

# Ejemplo de input: puedes modificar estos datos
personas = [
    'Ana', 'Luis', 'Juan', 'Sofía', 'Pedro', 'Marta', 'Carlos', 'Elena', 'Raúl', 'Lucía',
    'Diego', 'Valeria', 'Tomás', 'Paula', 'Andrés'
]
conexiones = [
    ('Ana', 'Luis'), ('Ana', 'Juan'), ('Ana', 'Pedro'),
    ('Luis', 'Sofía'), ('Juan', 'Pedro'), ('Pedro', 'Marta'),
    ('Marta', 'Carlos'), ('Carlos', 'Elena'), ('Elena', 'Raúl'),
    ('Raúl', 'Lucía'), ('Lucía', 'Diego'), ('Diego', 'Valeria'),
    ('Valeria', 'Tomás'), ('Tomás', 'Paula'), ('Paula', 'Andrés'),
    ('Andrés', 'Ana'), ('Carlos', 'Luis'), ('Elena', 'Juan'),
    ('Raúl', 'Sofía'), ('Lucía', 'Pedro'), ('Valeria', 'Carlos'),
    ('Tomás', 'Elena'), ('Paula', 'Raúl'), ('Andrés', 'Lucía')
]

# Análisis de la red
red = NetworkAnalysis(personas, conexiones)
valores, vectores = red.eigen_analysis()
valores = np.round(valores, 6)  # Redondear los autovalores

diagonal = np.diag(valores)
influencers = red.find_influencers(top_n=3)

# Generar informe
informe = generate_report(personas, influencers, red.adj_matrix, red.laplacian, valores, vectores)

with open('informe.txt', 'w', encoding='utf-8') as f:
    f.write(informe)

print('Informe generado: informe.txt')

draw_social_graph(personas, conexiones, influencers, filename='grafo.png', layout='kamada_kawai', adj_matrix=red.adj_matrix, laplacian=red.laplacian, diagonal=diagonal)

print('Se generó la imagen: grafo.png')
