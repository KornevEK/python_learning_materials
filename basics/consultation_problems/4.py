# Найти координаты элемента в матрице

n, m, element = map(int, input().split())

matrix = []

for _ in range(n):

    matrix.append(list(map(int, input().split())))

coords = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == element:
            coords.append([i, j])

if len(coords) == 0:
    print('not found')
    exit()
print(*coords)