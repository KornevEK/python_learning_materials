def gcd(a, b):
    # Recursive greatest common denominator
    # with Euclidean algorithm
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def leman(x):
    # Leman test for primality
    # Step 1
    for i in range(2, int(x ** (1 / 3)) + 1):
        if x % i == 0:
            return False
    # Step 2
    for k in range(1, int(x ** (1 / 3)) + 1):
        for d in range(int(x ** (1 / 6) / (4 * k ** 0.5)) + 2):
            D = (int((4 * k * x) ** 0.5) + d) ** 2 - 4 * k * x
            if D < 0:
                return True
            if int(D ** 0.5) ** 2 == D:
                A = int((4 * k * x) ** 0.5) + d
                B = int((A ** 2 - 4 * k * x) ** 0.5)
                d_ = gcd(A - B, x)
                if 1 < d_ < x:
                    return False

    return True


a = input()
a = int(a)

print(leman(a))