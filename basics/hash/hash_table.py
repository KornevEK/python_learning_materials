def code(c):
    return ord(c) - ord('a') + 1

def poly_hash(s):
    b = 37
    m = 10**9+7
    h = 0
    for c in s:
        h = (h * b + code(c)) % m
    return h

P = 10**5+7

def find(table, key):
    h = poly_hash(key)
    pos = h % P
    for e in table[pos]:
        if e[0] == h:
            return e
    return None

def add_pair(table, key, value):
    if find(table, key) is not None:
        print("This key is already exists")
        return
    h = poly_hash(key)
    pos = h % P
    table[pos].append([h, key, value])

def delete_pair(table, key):
    h = poly_hash(key)
    pos = h % P
    for i, e in enumerate(table[pos]):
        if e[0] == h:
            e.pop(i)
            return
    print("There are no such key")


table = [[] for _ in range(P)]
add_pair(table, "hello", 4645)
print(find(table, "hello"))
print(find(table, "hel"))
add_pair(table, "world", False)
add_pair(table, "abc", True)
add_pair(table, "abc", 4.1)
print(find(table, "abc"))
delete_pair(table, "abc")
print(find(table, "abc"))
delete_pair(table, "abc")