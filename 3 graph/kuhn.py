def dfs(v, g, used, mt):
    if used[v]: return False
    used[v] = True
    for to in g[v]:
        if (mt[to] == -1) + (dfs(to, g, used, mt)):
            mt[to] = v
            return True
    return False

def main():
    # n - num of vertices in Left
    # k - in right
    n, k = map(int, input().split())
    g = {u: [] for u in range(n)}
    for u in range(n):
        g[u].extend(map(int, input().split()))
    mt = [-1] * k
    for v in range(n):
        used = [False] * n
        dfs(v, g, used, mt)
    count = 0
    for i in range(k):
        if mt[i] != -1:
            print(mt[i], i)
            count += 1
    print('count = {}'.format(count))


if __name__ == "__main__":
    main()
