import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_social_graph(personas, conexiones, influencers, filename='grafo.png', layout='circular', adj_matrix=None, laplacian=None, diagonal=None):
    # Usar un grafo dirigido para mostrar flechas
    G = nx.DiGraph()
    G.add_nodes_from(personas)
    G.add_edges_from(conexiones)

    colores_nodos = ['red' if persona in influencers else 'skyblue' for persona in G.nodes()]

    plt.figure(figsize=(18, 10))
    if layout == 'circular':
        pos = nx.circular_layout(G)
    elif layout == 'spring':
        pos = nx.spring_layout(G, seed=42)
    elif layout == 'kamada_kawai':
        pos = nx.kamada_kawai_layout(G)
    elif layout == 'shell':
        pos = nx.shell_layout(G)
    else:
        pos = nx.random_layout(G)

    nx.draw(
        G, pos, with_labels=True, node_color=colores_nodos, node_size=1200,
        font_size=12, font_weight='bold', edge_color='gray', linewidths=2, arrows=True, arrowstyle='-|>', arrowsize=25
    )
    plt.title(f'Red Social e Influencers ({layout})', fontsize=16)

    # Formato: sin decimales para enteros, 3 decimales para floats, ancho fijo para columnas
    def format_number_fixed(v, width=7):
        if isinstance(v, (int, np.integer)) or (isinstance(v, float) and v.is_integer()):
            return f'{int(v):{width}d}'
        else:
            return f'{v:{width}.3f}'

    def matrix_to_multiline_str(matrix, compact=False, width=7):
        if compact:
            return '\n'.join(['[' + ','.join(format_number_fixed(v, width=width).strip() for v in row) + ']' for row in matrix])
        else:
            return '\n'.join(['[' + ','.join(format_number_fixed(v, width=width).strip() for v in row) + ']' for row in matrix])

    text_left = ""
    text_center = ""
    text_right = ""
    if adj_matrix is not None:
        text_left += "Matriz de adyacencia:\n" + matrix_to_multiline_str(adj_matrix, compact=True, width=3)
    if diagonal is not None:
        text_center += "Matriz diagonal (autovalores):\n" + matrix_to_multiline_str(diagonal, compact=True, width=9)
    if laplacian is not None:
        text_right += "Matriz laplaciana:\n" + matrix_to_multiline_str(laplacian, compact=True, width=4)
    # Ajuste de altura uniforme para las tres matrices
    y_pos = -0.18
    if text_left:
        plt.gcf().text(0.01, y_pos, text_left, fontsize=8, va='top', ha='left', family='monospace')
    if text_center:
        plt.gcf().text(0.36, y_pos, text_center, fontsize=8, va='top', ha='left', family='monospace')
    if text_right:
        plt.gcf().text(0.68, y_pos, text_right, fontsize=8, va='top', ha='left', family='monospace')
    plt.subplots_adjust(bottom=0.4)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
