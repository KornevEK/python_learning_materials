import time

def f(n):
    # recursive Fibonacci number computation
    if n == 0 or n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

n = int(input())
t0 = time.time()
fib_n = f(n)
t1 = time.time()
print(fib_n)
print('Recursive time:', t1 - t0)

t0 = time.time()
buff = [1, 1, 2]
for _ in range(n - 1):
    buff[2] = buff[1] + buff[0]
    buff[0] = buff[1]
    buff[1] = buff[2]
t1 = time.time()
print(buff[-1])
print('Memo time:', t1 - t0)