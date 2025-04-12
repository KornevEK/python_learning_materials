class Matrix:
    def __init__(self, a, m=None, n=None):
        if isinstance(a, list) and m is None:
            self.m = len(a)
            self.n = len(a[0])
            self.core = []
            for row in a:
                self.core.extend(row)
        elif m is not None:
            self.a = a.copy()
            self.m = m
            self.n = n
        elif isinstance(a, Matrix):
            self.m = a.m
            self.n = a.n
            self.core = a.core[:]
        self.size = len(self.core)

    def __repr__(self):
        res = ''
        for i in range(self.m):
            res += str(self.core[i*self.n:(i+1)*self.n]) + '\n'
        return res

    def __add__(self, other):
        res = Matrix(self)
        res.core = [self.core[i] + other.core[i] for i in range(self.size)]
        return res

# TODO implement determinant, matrix multiplication, system solving
if __name__ == '__main__':
    print('determinant test')
    inp = input()
    if inp != 'skip':
        row1 = list(map(int, inp.split()))
        n = len(row1)
        A = [row1]
        for _ in range(n-1):
            A.append(list(map(int, input().split())))
        A = Matrix(A)
        print(A.determinant())

    print('gauss test')
    inp = input()
    if inp != 'skip':
        row1 = list(map(int, inp.split()))
        n = len(row1)
        A = [row1]
        for _ in range(n-1):
            A.append(list(map(int, input().split())))
        A = Matrix(A)
        print('right hand side')
        b = list(map(int, input().split()))
        print('result')
        print(gauss_solve(A, b))

    print('multiplication test')
    print('matrix one')
    inp = input()
    if inp != 'skip':
        row1 = list(map(int, inp.split()))
        n = len(row1)
        A = [row1]
        for _ in range(n-1):
            A.append(list(map(int, input().split())))
        A = Matrix(A)
        print('matrix two')
        row1 = list(map(int, input().split()))
        n = len(row1)
        B = [row1]
        for _ in range(n-1):
            B.append(list(map(int, input().split())))
        B = Matrix(B)
        print('result')
        print(A @ B)

