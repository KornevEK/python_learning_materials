# Draw a pyramid in terminal

def pyramid(n, s):
    if n == 0:
        return []
    if n == 1:
        return [s]
    else:
        tmp = []
        for st in pyramid(n - 2, s):
            tmp.append(st + s)
        # print(tmp)
        return [s] + tmp + [s]
        # return [s] + [st + s for st in pyramid(n - 2)] + [s]

n, s = input().split()
n = int(n)

print(*pyramid(n, s), sep='\n')
