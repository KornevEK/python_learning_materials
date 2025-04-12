from math import floor

def heapify(a, i, L):
    left = 2 * i + 1
    right = 2 * i + 2
    mid = i # index of max elem of 3
    if left < L and a[left] < a[mid]:
        mid = left
    if right < L and a[right] < a[mid]:
        mid = right
    if mid != i:
        a[i], a[mid] = a[mid], a[i]
        heapify(a, mid, L)

def make_heap(a):
    L = len(a)
    for i in range(floor((L-2)/2), -1, -1):
        heapify(a, i, L)

def heap_sort(a):
    L = len(a)
    for i in range(L-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)
        
def is_heap(a):
    L = len(a)
    for i in range(L//2):
        if a[i] > a[2*i + 1] or a[i] > a[2*i + 2]:
            print('False')
            return
    print('True')

a = list(map(int, input().split()))
L = len(a)

is_heap(a)
make_heap(a)
print(*a)
is_heap(a)
