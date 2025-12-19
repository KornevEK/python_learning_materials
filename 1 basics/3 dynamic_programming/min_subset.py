def min_subset_in_range(values, l, u):
    dp = [0] + [float('inf')] * u
    prev = [0] + [-1] * u
    idx = [0] + [-1] * u
    for i, v in enumerate(sorted((v, i) for i, v in enumerate(values))):
        for j in range(u, v[0] - 1, -1):
            if dp[j - v[0]] + v[0] < dp[j]:
                dp[j] = dp[j - v[0]] + v[0]
                prev[j] = j - v[0]
                idx[j] = i
    weight = min((i for i in dp if l <= i), default=None)
    if weight is None:
        return None
    indices = []
    while weight > 0:
        indices.append(values[idx[weight]])
        weight = prev[weight]
    return sorted(indices)


n, l, u = map(int, input().split())
values = list(map(int, input().split()))
print(min_subset_in_range(values, l, u))