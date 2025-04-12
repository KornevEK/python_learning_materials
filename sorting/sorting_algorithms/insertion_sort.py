def insertion_sort(a):
    b = a.copy()
    for k in range(len(b) - 1):
        for i in range(k + 1):
            if b[k-i+1] < b[k-i]:
                b[k-i], b[k-i+1] = b[k-i+1], b[k-i]
            else:
                break
    return b