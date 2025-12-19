def merge(a, b):
    res = []
    while a and b:
        if a[0] <= b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    res.extend(a + b)
    return res

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        half = n // 2
        return \
            merge(merge_sort(arr[:half]), merge_sort(arr[half:]))
