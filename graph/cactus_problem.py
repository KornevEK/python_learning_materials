def dfs(u, adj_list, p, color, cycles):
    global flag
    flag = False
    color[u] = 1
    for v in adj_list[u].keys():
        if color[v] == 0:
            color[v] = 1
            p[v] = u
            dfs(v, adj_list, p, color, cycles)
            color[v] = 2
        elif color[v] == 1 and p[v] != u:
            adj_list[u][v] += 1
            adj_list[v][u] += 1
            if adj_list[u][v] > 1:
                flag = True
            v_ = u
            u_ = p[u]
            q = 2
            while u_ != v:
                q += 1
                v_ = u_
                u_ = p[u_]
                adj_list[u_][v_] += 1
                adj_list[v_][u_] += 1
                if adj_list[u][v] > 1:
                    flag = True
            cycles.append(q)
    color[u] = 2


def main():
    n, m = map(int, input().split())
    adj_list = {i: dict() for i in range(n)}
    for _ in range(m):
        route = list(map(int, input().split()))
        ki = route.pop(0)
        for i in range(ki-1):
            u = route[i] - 1
            v = route[i+1] - 1
            adj_list[u][v] = 0
            adj_list[v][u] = 0
    p = [-1] * n
    color = [0] * n
    cycles = []
    dfs(0, adj_list, p, color, cycles)
    print(cycles)
    if 0 in color:
        print(0)
        return
    if flag:
        print(0)
        return
    res = 1
    for c in cycles:
        if c != 2:
            res *= c+1
    print(res)


if __name__ == "__main__":
    main()
