# Check if the chess knight can go from
# cell (x1,y1) to (x2,y2) recursively in 2 moves

def move(x1, y1, x2, y2, count = 0, L = []):
    # Recursively move the knight and update the count
    # Don't put list as the default argument!!!

    # check if out of bounds
    if (x1 < 1) or (x1 >= 9) or (y1 < 1) or (y1 >= 9):
        return
    if count > 2:
        return
    if x1 == x2 and y1 == y2:
        L.append(count)
        return
    else:
        move(x1 - 1, y1 - 2, x2, y2, count + 1, L)
        move(x1 - 1, y1 + 2, x2, y2, count + 1, L)
        move(x1 + 1, y1 - 2, x2, y2, count + 1, L)
        move(x1 + 1, y1 + 2, x2, y2, count + 1, L)
        move(x1 - 2, y1 - 1, x2, y2, count + 1, L)
        move(x1 - 2, y1 + 1, x2, y2, count + 1, L)
        move(x1 + 2, y1 - 1, x2, y2, count + 1, L)
        move(x1 + 2, y1 + 1, x2, y2, count + 1, L)
        return

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

L = []
move(x1, y1, x2, y2, 0, L=L)

if len(L) == 0:
    print(-1)
else:
    print(min(L))
