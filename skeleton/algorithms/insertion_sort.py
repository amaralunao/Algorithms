def insertion_sort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        holder = i

        while holder > 0 and current < alist[holder-1]:
            alist[holder] = alist[holder-1]
            holder -= 1
        alist[holder] = current
    return alist
