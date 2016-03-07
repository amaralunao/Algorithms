from sys import argv
import random
import os
import importlib
from algorithms.singly_list import Node, UnorderedList


def load_time_memory():
    all_files = os.listdir('tests/python_profiling')[2:]
    path = "tests.python_profiling."
    module = importlib.import_module
    for name in all_files:
        name = name[:-3]
        module(path+name).profiling()


if __name__ == '__main__':
    name, size = argv
    random_list = random.sample(range(0, int(size)), int(size))
    huge_list = UnorderedList()
    for i in random_list:
        huge_list.append(i)
    load_time_memory()
