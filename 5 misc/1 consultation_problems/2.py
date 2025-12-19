# Решето Эратосфена

n = int(input())

a = list(range(n))

r = []

p = 2
k = 2

while p < n:
    if a[p] is None:
        p += 1
    else:
        r.append(a[p])
        k = a[p]
        while p < n:
            a[p] = None
            p += k
        p = k + 1

print(r)


