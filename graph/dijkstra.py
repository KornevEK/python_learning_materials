import time
def dijkstra(adj_list, weights, s, f, colors, lengths, prev):
    n = len(adj_list)
    lengths[s] = 0
    while True:
        min_l = float('inf')
        for u in range(n):
            if colors[u] == 'white' and lengths[u] < min_l:
                min_l = lengths[u]
                min_u = u
        if min_u == f:
            break
        colors[min_u] = 'black'
        for v in adj_list[min_u]:
            if colors[v] == 'white' and \
                    lengths[v] > lengths[min_u] + weights[frozenset([min_u, v])]:
                lengths[v] = lengths[min_u] + weights[frozenset([min_u, v])]
                prev[v] = min_u


if __name__ == "__main__":
    n, m, s, f = map(int, input().split())
    adj_list = [set() for u in range(n)]
    weights = dict()
    for e in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].add(v)
        adj_list[v].add(u)
        weights[frozenset([u, v])] = w
    colors = ['white' for u in range(n)]
    lengths = [float('inf') for u in range(n)]
    prev = [None for u in range(n)]

    t = time.time()
    dijkstra(adj_list, weights, s, f, colors, lengths, prev)
    print(time.time() - t, 'seconds, Dijkstra')

    res = [f]
    u_curr = f
    while u_curr != s:
        u_curr = prev[u_curr]
        res.append(u_curr)
    #print(*reversed(res))
    print(lengths[f])