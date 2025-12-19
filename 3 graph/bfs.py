# find if graph has cycle

from collections import deque
def bfs(init):
    colors[init] = 'black'
    queue.append(init)
    while queue:
        i = queue.popleft()
        colors[i] = 'black'
        for j in adj_list[i]:
            if j == init:
                return True
            if colors[j] == 'white':
                colors[j] = 'grey'
                queue.append(j)

if __name__ == "__main__":
    n, m = map(int, input().split())
    # множества смежных вершин для каждой вершины
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)
    queue = deque()
    colors = ['white'] * n

    for i in range(n):
        if bfs(i):
            print("CYCLE")
            break
    else:
        print("NO CYCLE")
