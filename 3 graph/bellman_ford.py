import time
def bellman_ford(edge_list, n, s):
    '''
    Performs Bellman-Ford algorithm
    https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
    :param edge_list: graph as the list of edges
    :param n: number of vertices
    :param s: index of starting vertex
    :return lengths: list of minimal weights
    '''
    lengths = [float('inf') for u in range(n)]
    lengths[s] = 0
    for _ in range(n-1):
        for edge in edge_list:
            u, v = edge[0]
            w = edge[1]
            if lengths[v] > lengths[u] + w:
                lengths[v] = lengths[u] + w
    return lengths

if __name__ == "__main__":
    '''
    n - number of vertices
    m - number of edges
    s - index of starting vertex
    f - index of final vertex
    '''
    n, m, s, f = map(int, input().split())
    edge_list = [] # contains a tuple (edge, weight)
    for e in range(m):
        u, v, w = map(int, input().split())
        edge_list.append(((u, v), w))
        edge_list.append(((v, u), w))
    t = time.time()
    lengths = bellman_ford(edge_list, n, s)
    print(time.time() - t, 'second, Bellman-Ford')
    print(lengths[f])