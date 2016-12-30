import timeit


def profiling():
    setup_insert = '''

from __main__ import (random_list, ordered_list, reversed_list, RBTree,
RBNode, BSTNode, BST)

binary_tree = BST()
red_black_tree = RBTree()

for i in ordered_list:
        binary_tree.insert(i)
for i in ordered_list:
        red_black_tree.insert(i)
def searching(alist):
    for i in alist:
        binary_tree.search(i)
def searching_rb(alist):
    for i in alist:
        red_black_tree.search(i)

    '''
    print('binary_tree search random time is:', timeit.timeit(
            "searching(random_list)", setup=setup_insert, number=1),
          '\nbinary_tree search ordered is:', timeit.timeit(
            "searching(ordered_list)", setup=setup_insert, number=1),
          '\nbinary_tree search reversed is:', timeit.timeit(
              "searching(reversed_list)", setup=setup_insert, number=1),
          '\nred_black_tree search random time is:', timeit.timeit(
            "searching_rb(random_list)", setup=setup_insert, number=1),
          '\nred_black_tree search ordered is:', timeit.timeit(
            "searching_rb(ordered_list)", setup=setup_insert, number=1),
          '\nred_black_tree search reversed is:', timeit.timeit(
            "searching_rb(reversed_list)", setup=setup_insert, number=1))
