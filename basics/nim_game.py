from math import log2, floor
def xor(a):
    res = 0
    for e in a:
        res = res ^ e
    return res

if __name__ == "__main__":

    a = list(map(int, input("Enter bunches: ").split()))

    S = xor(a)

    if S != 0:
        print("The first wins")
    else:
        print("The second wins")

    while sum(a) > 0:
        print(*a)

        S = xor(a)

        if S == 0:
            print("No winning turn")
        else:
            big_bit = floor(log2(S))
            for i, e in enumerate(a):
                if len(bin(e)[2:]) > big_bit and bin(e)[2:][::-1][big_bit] == '1':
                    break
            b = a[i] ^ S
            print(f"From {i}'th bunch take {a[i] - b} matches")
        while True:
            try:
                i, c = map(int, input("Bunch no., amount: ").split())
                if a[i] - c < 0 or c < 1:
                    print("Incorrect turn")
                    raise ValueError
                a[i] -= c
            except:
                print("try again")
                continue
            break
        print()
    print("You won")
