import random
import time

from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.radix_sort import radix_sort

def is_sorted(arr):
    return not bool(sum([(arr[i] > arr[i + 1]) for i in range(len(arr) - 2)]))

n = int(input())

arr = [random.randint(0, 10 ** 10) for _ in range(n)]
#arr = [i for i in range(n - 1, -1, -1)]

t0 = time.time()
insertion_sort(arr)
t1 = time.time()
merge_sort(arr)
t2 = time.time()
quick_sort(arr)
t3 = time.time()
radix_sort(arr)
t4 = time.time()

print('Insertion', t1-t0)
print('Merge    ', t2-t1)
print('Quick    ', t3-t2)
print('Radix    ', t4-t3)
