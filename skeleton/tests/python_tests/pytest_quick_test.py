from algorithms.quick_sort import quick_sort
from .is_sorted_test import is_sorted


def test_quick_sort_random(random_list):
    assert is_sorted(quick_sort(random_list)) is True


def test_quick_sort_empty(empty_list):
    assert is_sorted(quick_sort(empty_list)) is True


def test_quick_sort_one(one_list):
    assert is_sorted(quick_sort(one_list)) is True


def test_quick_sort_sorted(sorted_list):
    assert is_sorted(quick_sort(sorted_list)) is True


def test_quick_sort_reverse_sorted(reverse_sorted):
    assert is_sorted(quick_sort(reverse_sorted)) is True
