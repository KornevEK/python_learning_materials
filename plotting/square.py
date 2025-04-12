from matplotlib import pyplot as plt

def draw_square(A, B, C, D):

    x = [A[0], B[0], C[0], D[0], A[0]]
    y = [A[1], B[1], C[1], D[1], A[1]]

    plt.plot(x, y, 'k')
def divide(A, B, r):

    C = ((1 / r) * A[0] + (1 - 1 / r) * B[0],
         (1 / r) * A[1] + (1 - 1 / r) * B[1])

    return C

if __name__ == "__main__":

    r = float(input("ratio = "))
    n = int(input("num of squares = "))

    A = (0, 0)
    B = (0, 1)
    C = (1, 1)
    D = (1, 0)

    for _ in range(n):
        draw_square(A, B, C, D)
        A, B, C, D = divide(A, B, r), \
                     divide(B, C, r), \
                     divide(C, D, r), \
                     divide(D, A, r)

    plt.axis('equal')
    plt.savefig('square.png', dpi=300)
    plt.show()