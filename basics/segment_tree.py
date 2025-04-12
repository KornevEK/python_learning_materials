import math as m
from operator import add, mul

def build_recursive(t, a, i, tl, tr, function):
    if tr - tl == 1:
        t[i] = a[tl]
    else:
        tm = (tl + tr) // 2
        build_recursive(t, a, 2*i+1, tl, tm, function)
        build_recursive(t, a, 2*i+2, tm, tr, function)
        if t[2*i+1] is not None and t[2*i+2] is not None:
            t[i] = function(t[2*i+1], t[2*i+2])
        elif t[2*i+1] is None or t[2*i+2] is None:
            if t[2*i+1] is not None:
                t[i] = t[2*i+1]
            else:
                t[i] = t[2*i+2]

def build(a, function):
    h = m.ceil(m.log2(len(a)))
    b = a.copy()
    b.extend([None for _ in range(2 ** h - len(a))])
    t = [None for _ in range(2 ** (h + 1) - 1)]
    build_recursive(t, b, i=0, tl=0, tr=len(b), function=function)
    return t

def request_recursive(t, tl, tr, function, i=0):
    h = m.ceil(m.log2(len(t)))
    h_current = m.floor(m.log2(i + 1))
    length = 2 ** (h - 1 - h_current)
    left = i
    left = left * (2**(h-h_current-1)) + 2**(h-h_current-1) - 1
    left = left-(2**(h-1)-1)
    right = left + length
    if tl <= left and tr >= right:
        return t[i]
    if tr <= left or tl >= right:
        return None
    res_left = request_recursive(t, tl, tr, function, i=2*i+1)
    res_right = request_recursive(t, tl, tr, function, i=2*i+2)
    if res_left is not None and res_right is not None:
        return function(res_left, res_right)
    elif res_left is None or res_right is None:
        if res_left is not None:
            return res_left
        else:
            return res_right

f = mul

a = [1, 5, 4, 7, 4, 1, 9, 8, 5, 6]
t = build(a, f)
print(t)

print(request_recursive(t, 0, len(a)+1, f))
print(request_recursive(t, 0, 1, f))
print(request_recursive(t, 2, 3, f))
print(request_recursive(t, 0, 5, f))