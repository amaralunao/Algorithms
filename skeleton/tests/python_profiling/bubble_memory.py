import copy
from algorithms.bubble_sort import bubble_sort
from memory_profiler import profile
from . import lists


test_list = copy.copy(lists.huge_list)


@profile
def memory():
        return bubble_sort(test_list)

if __name__ == '__main__':
    memory()
