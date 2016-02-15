def merge_sort2(A):
    B = list(range(0, len(A)))
    split_merge(A, 0, len(A), B)
    return A


def split_merge(A, begin, end, B):
    if (end - begin) < 2:
        return
    else:
        middle = (end + begin) // 2
        split_merge(A, begin, middle, B)
        split_merge(A, middle, end, B)
        merge(A, begin, middle, end, B)
        copy_list(B, begin, end, A)


def merge(A, begin, middle, end, B):

    i = begin
    j = middle

    for k in range(begin, end):
        if i < middle and (j >= end or A[i] <= A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1


def copy_list(B, begin, end, A):

        for k in range(begin, end):
            A[k] = B[k]
