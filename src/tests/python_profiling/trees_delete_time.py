import timeit


def profiling():
    setup_delete = '''

from __main__ import (random_list, ordered_list, reversed_list, RBTree,
RBNode, BSTNode, BST)

binary_tree = BST()
for i in random_list:
   binary_tree.insert(i)
def deleting(list):
   for i in list:
       binary_tree.delete(i)

red_black_tree = RBTree()
for i in random_list:
   red_black_tree.insert(i)
def deleting_rb(list):
   for i in list:
       red_black_tree.delete(i)

    '''
    print('binary_tree delete random time is:', timeit.timeit(
            "deleting(random_list)", setup=setup_delete, number=1),
          '\nbinary_tree delete ordered time is:', timeit.timeit(
            "deleting(ordered_list)", setup=setup_delete, number=1),
          '\nbinary_tree delete reversed time is:', timeit.timeit(
            "deleting(reversed_list)", setup=setup_delete, number=1),
          '\nred_black_tree delete reversed time is:', timeit.timeit(
            "deleting_rb(reversed_list)", setup=setup_delete, number=1),
          '\nred_black_tree delete ordered time is:', timeit.timeit(
             "deleting_rb(ordered_list)", setup=setup_delete, number=1),
          '\nred_black_tree delete reversed time is:', timeit.timeit(
              "deleting_rb(reversed_list)", setup=setup_delete, number=1))
