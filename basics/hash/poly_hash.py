def code(c):
    return ord(c) - ord('a') + 1

def poly_hash(s):
    b = 37
    m = 10**9+7
    h = 0
    for c in s:
        h = (h * b + code(c)) % m
    return h


s = input()
print(poly_hash(s))