import random
from .memory_decorator import profiles


@profiles
def quick_sort(alist):
    quick_help(alist, 0, len(alist) - 1)
    return alist


def quick_help(alist, start, stop):
    if stop - start > 0:
        pivot = alist[random.randint(start, stop)]
        left = start
        right = stop
        while left <= right:
            while alist[left] < pivot:
                left += 1
            while alist[right] > pivot:
                right -= 1
            if left <= right:
                alist[left], alist[right] = alist[right], alist[left]
                left += 1
                right -= 1
        quick_help(alist, start, right)
        quick_help(alist, left, stop)
