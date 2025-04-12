import time

def cubes(n=None):
    i = 0
    while True:
        yield i**3
        i += 1
        if n is not None and i == n:
            return

if __name__ == "__main__":

    gen = cubes(20)

    for _ in range(10):
        print(next(gen))

    print("STOP")

    for _ in range(20):
        print(next(gen, "EMPTY"))
