# Writing custom functions for lists

def my_max(a):
    if len(a) == 0:
        return 0
    else:
        max_value = a[0]
        for value in a:
            if value > max_value:
                max_value = value
        return max_value

def my_sort(a):
    b = a.copy()
    for k in range(len(b) - 1):
        for i in range(k + 1):
            if b[k-i+1] < b[k-i]:
                b[k-i], b[k-i+1] = b[k-i+1], b[k-i]
            else:
                break
    return b

def transpose(a):
    # Transpose a square matrix
    a = a.copy()
    for i in range(n):
        for j in range(n):
            if i < j:
                a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

# Read a square matrix
a0 = list(map(int, input().split()))
n = len(a0)
a = [0] * n
a[0] = a0

for i in range(1, n):
    a[i] = list(map(int, input().split()))
a_t = transpose(a)

for s in a_t:
    print(s)