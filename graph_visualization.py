import networkx as nx
import matplotlib.pyplot as plt

def draw_social_graph(people, connections, influencers, filename='grafo.png'):
    G = nx.Graph()
    G.add_nodes_from(people)
    G.add_edges_from(connections)

    # Colores: influencers en rojo, otros en azul
    node_colors = ['red' if person in influencers else 'skyblue' for person in G.nodes()]

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=12, font_weight='bold', edge_color='gray')
    plt.title('Red Social e Influencers')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
