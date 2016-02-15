
def merge_sort_slow(alist):
    inputsize = len(alist)
    if inputsize <= 1:
        return alist
    else:
        mid_index = inputsize // 2
        left = alist[0:mid_index]
        right = alist[mid_index:]
        left = merge_sort_slow(left)
        right = merge_sort_slow(right)
        return copy_list(alist, merge(left, right))


def merge(left, right):
    result = []
    while (len(left) > 0 and left is not None) or \
            (len(right) > 0 and right is not None):
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif left is not None and len(left) > 0:
            result.append(left[0])
            left.pop(0)
        elif right is not None and len(right) > 0:
            result.append(right[0])
            right.pop(0)

    return result


def copy_list(A, B):
    if len(A) == len(B):
        for k in range(0, len(A)):
            A[k] = B[k]
    return A
