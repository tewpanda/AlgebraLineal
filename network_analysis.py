import numpy as np

class NetworkAnalysis:
    def __init__(self, people, connections):
        self.people = people
        self.connections = connections
        self.adj_matrix = self.create_adjacency_matrix()
        self.laplacian = self.create_laplacian_matrix()

    def create_adjacency_matrix(self):
        n = len(self.people)
        matrix = np.zeros((n, n), dtype=int)
        for a, b in self.connections:
            i = self.people.index(a)
            j = self.people.index(b)
            matrix[i][j] = 1
            matrix[j][i] = 1  # undirected
        return matrix

    def create_laplacian_matrix(self):
        degree = np.diag(np.sum(self.adj_matrix, axis=1))
        return degree - self.adj_matrix

    def eigen_analysis(self):
        vals, vecs = np.linalg.eigh(self.laplacian)
        return vals, vecs

    def find_influencers(self, top_n=3):
        centrality = np.sum(self.adj_matrix, axis=1)
        indices = np.argsort(-centrality)[:top_n]
        return [self.people[i] for i in indices]
