# our for

a = [0, 1, 2, 3]
a = iter(a)

while True:
    try:
        i = a.__next__()
        print(i)
    except StopIteration:
        break
