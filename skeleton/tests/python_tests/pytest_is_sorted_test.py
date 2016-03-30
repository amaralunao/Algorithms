
def is_sorted(alist):
    cnt = 0
    while cnt < len(alist) - 1:
        if alist[cnt] < alist[cnt+1]:
            cnt += 1
        else:
            return False
    return True


def test_is_sorted_empty(empty_list):
    assert is_sorted(empty_list) is True


def test_is_sorted_one(one_list):
    assert is_sorted(one_list) is True


def test_is_sorted_sorted(sorted_list):
    assert is_sorted(sorted_list) is True
