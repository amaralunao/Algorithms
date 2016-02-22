from sys import argv
import random
import os
import importlib


def load_time_memory():
    all_files = os.listdir('tests/python_profiling')[2:]
    path = "tests.python_profiling."
    module = importlib.import_module
    for name in all_files:
        name = name[:-3]
        module(path+name).profiling()


if __name__ == '__main__':
    name, size = argv
    huge_list = random.sample(range(0, int(size)), int(size))
    load_time_memory()
