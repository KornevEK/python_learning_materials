# A 2D cell game where the target is to reach the 'key' cell
# and then get to the 'target' cell

# Enter target coordinates:
# 5 5
# Enter key coordinates:
# 3 3
# Enter the moving sequence:
# wdwdwd
# ( 3 3 )
# Enter the moving sequence:
# Key obtained!
# wdwd
# ( 5 5 )
# You won!

print("Enter target coordinates:")
x_target, y_target = input().split()
x_target = int(x_target)
y_target = int(y_target)

print("Enter key coordinates:")
x_key, y_key = input().split()
x_key = int(x_key)
y_key = int(y_key)

x = 0
y = 0
hasKey = False
while not (x == x_target and y == y_target and hasKey):
    print("Enter the moving sequence:")
    if x == x_key and y == y_key:
        hasKey = True
        print("Key obtained!")
    for c in input():
        if c == 'w':
            y += 1
        elif c == 's':
            y -= 1
        elif c == 'a':
            x -= 1
        elif c == 'd':
            x += 1
        else:
            print("Incorrect input")
    print('(', x, y, ')')

print("You won!")
