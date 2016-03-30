from algorithms.bubble_sort import bubble_sort
from .is_sorted_test import is_sorted


def test_bubble_sort_random(random_list):
    assert is_sorted(bubble_sort(random_list)) is True


def test_bubble_sort_one(one_list):
    assert is_sorted(bubble_sort(one_list)) is True


def test_bubble_sort_sorted(sorted_list):
    assert is_sorted(bubble_sort(sorted_list)) is True


def test_bubble_sort_reverse_sorted(reverse_sorted):
    assert is_sorted(bubble_sort(reverse_sorted)) is True


def test_bubble_sort_empty(empty_list):
    assert is_sorted(bubble_sort(empty_list)) is True
