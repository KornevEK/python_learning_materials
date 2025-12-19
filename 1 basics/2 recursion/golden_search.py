def find_max(func, x0, x3, epsilon = 1e-6):
    # find maximum of a function with a golden-section search
    # in bounds recursively
    if (x3 - x0) < epsilon:
        return (x0 + x3) / 2
    else:
        x1 = x0 + (x3 - x0) / 3
        x2 = x1 + (x3 - x0) / 3
        if func(x1) < func(x2):
            return find_max(func, x1, x3, epsilon)
        else:
            return find_max(func, x0, x2, epsilon)

import math as m

def func(z):
    if z <= 1:
        return z
    else:
       return 1.5 - z / 2

x = find_max(func, -100, 100)
print(x)
print(func(x))
