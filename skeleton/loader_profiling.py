from sys import argv
import random
import importlib
from tests.python_profiling import lists

name, size = argv

lists.huge_list = random.sample(range(0, int(size)), int(size))


def load_time_memory():
    path = "tests.python_profiling."
    names = ["bubble_memory", "bubble_time", "insertion_memory", "insertion_time",
            "merge_memory_slow", "merge_memory2", "merge_time_slow", "merge_time2"]

    for name in names:
        if "_memory" in name:
            print(importlib.import_module(path + name).memory())
        else:
            print(importlib.import_module(path + name).time())


if __name__ == '__main__':
    load_time_memory()
