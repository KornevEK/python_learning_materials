import time
from network import draw
from matplotlib import pyplot as plt


def find(i):
    indices = []
    while p[i][0] != -1:
        indices.append(i)
        i = p[i][0]
    for j in indices[:-1]:
        p[j][0] = i
    return i


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    p = [[-1, 1] for _ in range(n)]
    # заполняем вспомогательные структуры
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    edges.sort(key=lambda x: x[2])
    tree_weight = 0
    tree = []
    # пробегаем по рёбрам
    t0 = time.time()
    for u, v, w in edges:
        set_u = find(u)
        set_v = find(v)
        if set_u != set_v:
            if p[set_v][1] < p[set_u][1]:
                p[set_v][0] = set_u
                p[set_u][1] = p[set_u][1] + p[set_v][1]
            else:
                p[set_u][0] = set_v
                p[set_v][1] = p[set_u][1] + p[set_v][1]
            tree_weight += w
            tree.append([u, v])
        if len(tree) == n-1:
            break
    t1 = time.time()
    print(t1 - t0, "seconds")

    draw(edges, tree=tree)
    plt.savefig("graph.png", dpi=200) # до show!
    plt.show()
