import timeit


def profiling():
    setup_insert = '''

from __main__ import (random_list, ordered_list, reversed_list, RBTree,
RBNode, BSTNode, BST)

binary_tree = BST()
red_black_tree = RBTree()
def insert_binary(alist):
    for i in alist:
        binary_tree.insert(i)

def insert_red_black(alist):
    for i in alist:
        red_black_tree.insert(i)

    '''
    print('binary_tree insert random time is:', timeit.timeit(
            "insert_binary(random_list)", setup=setup_insert, number=1),
          '\nbinary_tree insert ordered is:', timeit.timeit(
            "insert_binary(ordered_list)", setup=setup_insert, number=1),
          '\nbinary_tree insert reversed is:', timeit.timeit(
              "insert_binary(reversed_list)", setup=setup_insert, number=1),
          '\nred_black_tree insert random time is:', timeit.timeit(
            "insert_red_black(random_list)", setup=setup_insert, number=1),
          '\nred_black_tree insert ordered is:', timeit.timeit(
            "insert_red_black(ordered_list)", setup=setup_insert, number=1),
          '\nred_black_tree insert reversed is:', timeit.timeit(
            "insert_red_black(reversed_list)", setup=setup_insert, number=1))
