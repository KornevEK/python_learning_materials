from collections import deque

def bfs(s, t, adj_list):
    q = deque()
    q.append(s)
    visited = {key: False for key in adj_list.keys()}
    visited[s] = True
    prev = {key: None for key in adj_list.keys()}
    while q:
        u = q.popleft()
        for v in adj_list[u].keys():
            if not visited[v] and adj_list[u][v]:
                prev[v] = u
                q.append(v)
                visited[v] = True
                if v == t:
                    c_min = float('inf')
                    path = []
                    while prev[v] is not None:
                        c_min = min(c_min, adj_list[prev[v]][v])
                        path.append(v)
                        v = prev[v]
                    path.append(s)
                    return path[::-1], c_min
    return [], 0


if __name__ == "__main__":
    m = int(input())
    adj_list = {}
    for _ in range(m):
        u, v, c = input().split()
        c = int(c)
        adj_list.setdefault(u, {})
        adj_list[u][v] = c
        adj_list.setdefault(v, {})
        adj_list[v][u] = 0
    flow = 0
    while True:
        path, c = bfs('S', 'T', adj_list)
        print(path)
        if not path:
            break
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            adj_list[u][v] -= c
            adj_list[v][u] += c
        flow += c
    print(flow)