from network_analysis import NetworkAnalysis
from report import generate_report
from graph_visualization import draw_social_graph
import numpy as np

# Solicitar input desde la terminal (solo la lista de personas y la lista de conexiones)
personas = eval(input('Pega la lista de personas (ejemplo: ["Ana", "Luis", ...]):\n'))
conexiones = eval(input('Pega la lista de conexiones (ejemplo: [("Ana", "Luis"), ("Ana", "Juan"), ...]):\n'))

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
