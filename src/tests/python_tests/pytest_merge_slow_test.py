from algorithms.merge_sort_slow import merge_sort_slow
from .is_sorted_test import is_sorted


def test_merge_sort_slow_random(random_list):
    assert is_sorted(merge_sort_slow(random_list)) is True


def test_merge_sort_slow_empty(empty_list):
    assert is_sorted(merge_sort_slow(empty_list)) is True


def test_merge_sort_slow_one(one_list):
    assert is_sorted(merge_sort_slow(one_list)) is True


def test_merge_sort_slow_sorted(sorted_list):
    assert is_sorted(merge_sort_slow(sorted_list)) is True


def test_merge_sort_slow_reverse_sorted(reverse_sorted):
    assert is_sorted(merge_sort_slow(reverse_sorted)) is True
