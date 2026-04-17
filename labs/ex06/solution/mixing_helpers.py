import networkx
import numpy as np

n_nodes = 16
def generate_torus_adj_matrix(n_nodes):
    G = networkx.generators.lattice.grid_2d_graph(int(np.sqrt(n_nodes)), int(np.sqrt(n_nodes)), periodic=True)
    # Adjacency matrix
    A = networkx.adjacency_matrix(G).toarray()

    # Add self-loops
    for i in range(0, A.shape[0]):
        A[i][i] = 1
    return A