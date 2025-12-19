# Famous bug problem

a = list(map(int, input().split()))
a = [0] + a
n = len(a)

b = [0] * n
c = [0] * n

b[1] = a[1]
c[1] = 0
for i in range(2, n):
    b[i] = min(b[i-1], b[i-2]) + a[i]
    if b[i-1] < b[i-2]:
        c[i] = i-1
    else:
        c[i] = i-2

print(b[-1])

ind = n-1
res = [n-1]
while ind != 0:
    res.append(c[ind])
    ind = c[ind]
res.reverse()
print(res)
