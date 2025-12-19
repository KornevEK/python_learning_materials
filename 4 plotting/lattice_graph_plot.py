from collections import deque
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def trunc_index(i, j):
    if i == -1 or i == n:
        return False
    if j == -1 or j == m:
        return False
    return True


if __name__ == "__main__":

    n, m, n_parts = map(int, input().split())
    N = n*m

    A = np.zeros((N, N), dtype=int)
    for i in range(n):
        for j in range(m):
            mi = i * m + j
            for di in (-1, 1):
                if trunc_index(i+di, j):
                    mi_neigh = (i+di) * m + j
                    A[mi, mi_neigh] = 1
            for dj in (-1, 1):
                if trunc_index(i, j+dj):
                    mi_neigh = i * m + j + dj
                    A[mi, mi_neigh] = 1
    A = (np.ones((N, N), dtype=int) - np.eye(N, dtype=int)) * A

    pos = [np.unravel_index(mi, (n, m)) for mi in range(N)]
    G = nx.from_numpy_array(A)
    nx.draw(G, pos=pos)
    plt.savefig('grid.png', dpi=200)
    plt.show()
