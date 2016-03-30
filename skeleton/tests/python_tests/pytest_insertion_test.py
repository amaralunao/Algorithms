from algorithms.insertion_sort import insertion_sort
from .is_sorted_test import is_sorted


def test_insertion_sort_random(random_list):
    assert is_sorted(insertion_sort(random_list)) is True


def test_insertion_sort_empty(empty_list):
    assert is_sorted(insertion_sort(empty_list)) is True


def test_insertion_sort_one(one_list):
    assert is_sorted(insertion_sort(one_list)) is True


def test_insertion_sort_sorted(sorted_list):
    assert is_sorted(insertion_sort(sorted_list)) is True


def test_insertion_sort_reverse_sorted(reverse_sorted):
    assert is_sorted(insertion_sort(reverse_sorted)) is True
