# Отсортировать числа по первой цифре

def w_sort(a):

    a_str = list(map(str, a))

    s = [[] for _ in range(10)]

    for number in a_str:
        index = (ord(number[0]) + 2) % 10
        s[index].append(number)

    counter = 0
    for lst in s:
        for number in lst:
            a[counter] = int(number)
            counter += 1

a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(*a)

w_sort(a)

print(*a)

