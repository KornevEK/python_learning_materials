# задача про вора

a = list(map(int, input().split()))

n = len(a)

Bp = [0] * n
Bm = [0] * n

Bp[0] = a[0]

for i in range(n - 1):

    Bp[i + 1] = Bm[i] + a[i + 1]
    Bm[i + 1] = max(Bp[i], Bm[i])

print(max(Bp[-1], Bm[-1]))


