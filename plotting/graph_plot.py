import networkx as nx
import matplotlib.pyplot as plt

print('Визуализация графа, заданного как список рёбер')
print('Граф ориентированный? (yes/[no])')
if input() == 'yes':
    G = nx.DiGraph()
else:
    G = nx.Graph()
print('Введите число рёбер графа')
n = int(input())
print(f'Введите {n} пар вершин в формате "i j"')
for _ in range(n):
    i, j = input().split()
    i, j = int(i), int(j)
    G.add_edge(i, j)

nx.draw_networkx(G)
plt.show()
