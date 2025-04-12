# deterministic quicksort without pivoting
# breaks on reverse sorted arrays
def quick_sort_part(arr, low, high):
    l = low
    h = high

    if low < high:
        while l != h:
            if arr[l] <= arr[h]:
                l += 1
            else:
                arr[l], arr[h-1], arr[h] = arr[h-1], arr[h], arr[l]
                h -= 1
        quick_sort_part(arr, low, l-1)
        quick_sort_part(arr, l+1, high)


def quick_sort(arr):
    a = arr.copy()
    quick_sort_part(a, 0, len(a)-1)
    return a

