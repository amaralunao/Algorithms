from algorithms.merge_sort2 import merge_sort2
from .is_sorted_test import is_sorted


def test_merge_sort2_random(random_list):
    assert is_sorted(merge_sort2(random_list)) is True


def test_merge_sort2_empty(empty_list):
    assert is_sorted(merge_sort2(empty_list)) is True


def test_merge_sort2_one(one_list):
    assert is_sorted(merge_sort2(one_list)) is True


def test_merge_sort2_sorted(sorted_list):
    assert is_sorted(merge_sort2(sorted_list)) is True


def test_merge_sort2_reverse_sorted(reverse_sorted):
    assert is_sorted(merge_sort2(reverse_sorted)) is True
