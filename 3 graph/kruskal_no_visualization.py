import networkx as nx
from matplotlib import pyplot as plt
def find_root(p, u):
    while p[u] != u:
        u = p[u]
    return u
def is_united(p, u, v):
    root_u = find_root(p, u)
    root_v = find_root(p, v)
    if root_u != root_v:
        return False
    else:
        p[u] = root_u
        p[v] = root_u
        return True
def unite(p, u, v):
    root_u = find_root(p, u)
    root_v = find_root(p, v)
    p[root_u] = root_v

def draw_graph():
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges)
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

if __name__ == "__main__":
    n, m = map(int, input().split())
    edge_list = [] # contains a tuple ((u, v), weight)
    G = nx.Graph()
    for edge in range(m):
        u, v, w = map(int, input().split())
        edge_list.append(((u, v), w))
    G.add_weighted_edges_from([(e[0][0], e[0][1], e[1]) for e in edge_list])
    pos = nx.spring_layout(G, seed=7)
    edge_labels = nx.get_edge_attributes(G, "weight")
    plt.figure(figsize=(20, 15))
    draw_graph()
    plt.figure(figsize=(20, 15))
    plt.pause(1)
    edge_list.sort(key=lambda edge: edge[1])
    p = list(range(n))
    w_total = 0
    edges_total = []
    for edge in edge_list:
        u = edge[0][0]
        v = edge[0][1]
        w = edge[1]
        if not is_united(p, u, v):
            unite(p, u, v)
            w_total += w
            edges_total.append((u, v))
            plt.close()
            plt.figure(figsize=(20, 15))
            draw_graph()
            nx.draw_networkx_edges(G, pos, edgelist=edges_total, edge_color='r', width=10)
            plt.pause(1)
            if len(edges_total) == n - 1:
                break
    draw_graph()
    nx.draw_networkx_edges(G, pos, edgelist=edges_total, edge_color='r')
    plt.show()
    print(w_total)
    for edge in edges_total:
        print(*edge)