import random

def radix_sort_part(arr, position):
    d = {c : [] for c in '0123456789'}
    for e in arr:
        c = e[position]
        d[c].append(e)
    res = []
    for c in '0123456789':
        res.extend(d[c])
    return res

def radix_sort(arr):
    a = list(map(str, arr))
    len_max = max(map(len, a))
    a = ['0' * (len_max - len(e)) + e for e in a]
    for position in range(len_max - 1, - 1, - 1):
        a = radix_sort_part(a, position)
    return list(map(int, a))