import networkx as nx
import matplotlib.pyplot as plt

def draw_social_graph(personas, conexiones, influencers, filename='grafo.png', layout='circular'):
    # Usar un grafo dirigido para mostrar flechas
    G = nx.DiGraph()
    G.add_nodes_from(personas)
    G.add_edges_from(conexiones)

    colores_nodos = ['red' if persona in influencers else 'skyblue' for persona in G.nodes()]

    plt.figure(figsize=(10, 8))
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
    # plt.tight_layout()  # Comentado para evitar la advertencia
    plt.savefig(filename)
    plt.close()
