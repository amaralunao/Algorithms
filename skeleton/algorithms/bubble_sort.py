def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1, i, -1):
            if alist[j] < alist[j-1]:
                holder = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = holder
            else:
                pass
    return alist
