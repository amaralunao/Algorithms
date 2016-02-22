import copy
from algorithms.insertion_sort import insertion_sort
from memory_profiler import profile
from . import lists


test_list = copy.copy(lists.huge_list)

@profile
def memory():
    return insertion_sort(test_list)


if __name__ == '__main__':
    memory()
