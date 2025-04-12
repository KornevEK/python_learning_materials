# Dynamic programming for the knapsack problem

capacity = int(input())
n = int(input())
a = []

for _ in range(n):
    a.append(tuple(map(int, input().split())))

m = [[0] * capacity for _ in range(n)]

for i in range(n):
    for j in range(capacity):
        if a[i][0] > j:
            m[i][j] = m[i - 1][j]
        else:
            m[i][j] = max(m[i - 1][j], m[i - 1][j - a[i][0]] + a[i][1])

print(m[-1][-1])
