import math
from pytest import raises
from algorithms.red_black_tree import RED, BLACK


def is_height_correct(tree):

    if tree._height(tree.root) <= 2*math.log2(tree._node_count(tree.root) + 1):
        return True
    else:
        return False


def test_search_empty(empty):
    with raises(KeyError):
        empty.search(7)


def test_search_found_one(one):
    assert one.search(5) == one.root.key


def test_search_not_found_one(one):
    with raises(KeyError):
        one.search(7)


def test_search_found_five_right(five_right):
    assert five_right.search(2) == five_right.root.left.key


def test_is_height_correct_one(one):
    assert is_height_correct(one) is True


def test_is_height_correct_five_left(five_left):
    assert is_height_correct(five_left) is True


def test_is_height_correct_five_right(five_right):
    assert is_height_correct(five_right) is True


def test_insert_empty(empty):
    assert empty.insert(5) is True
    assert empty.root.key == 5
    assert empty.root.color == BLACK


def test_insert_right_one_BST(one):
    assert one.insert(7) is True
    assert one.root.right.key == 7
    assert one.root.right.color == RED


def test_insert_left_one_BST(one):
    assert one.insert(3)
    assert one.root.left.key == 3
    assert one.root.left.color == RED


def test_insert_case1_five_left(five_left):
    assert five_left.insert(1) is True
    assert five_left.root.left.left.left.key == 1
    assert five_left.root.left.left.left.color == RED
    assert five_left.root.color == BLACK
    assert five_left.root.left.left.color == BLACK
    assert five_left.root.left.right.color == BLACK


def test_insert_case3_five_left(five_left):
    five_left.insert(1)
    assert five_left.insert(0) is True
    assert five_left.root.left.left.left.key == 0
    assert five_left.root.left.left.left.color == RED
    assert five_left.root.left.left.key == 1
    assert five_left.root.left.left.color == BLACK


def test_insert_case2_five_right(five_right):
    five_right.insert(8)
    assert five_right.insert(9) is True
    assert five_right.root.right.right.right.key == 9
    assert five_right.root.right.right.right.color == RED
    assert five_right.root.right.right.color == BLACK
    assert five_right.root.right.right.key == 8


def test_delete_not_found(one):
    with raises(KeyError):
        one.delete(0)


def test_delete_case_1(empty):
    empty.insert(1)
    empty.insert(2)
    assert empty.delete(1) is True
    assert empty.root.key == 2
    assert empty.root.color == BLACK
    assert is_height_correct(empty) is True


def test_delete_case_1_2_left(empty, nodes1):
    for key in nodes1:
        empty.insert(key)
    assert empty.delete(15) is True
    assert empty.root.color == BLACK
    assert is_height_correct(empty) is True


def test_delete_case_3_4_left(empty, nodes1):
    for key in nodes1:
        empty.insert(key)
    assert empty.delete(7) is True
    assert empty.root.color == BLACK
    assert is_height_correct(empty) is True


def test_delete_case_1_2_right(empty, nodes2):
    for key in nodes2:
        empty.insert(key)
    assert empty.delete(9) is True
    assert empty.root.color == BLACK
    assert is_height_correct(empty) is True


def test_delete_case_3_4_right(empty, nodes2):
    for key in nodes2:
            empty.insert(key)
    assert empty.delete(10) is True
    assert empty.root.color == BLACK
    assert is_height_correct(empty) is True


def test_delete_huge_list(empty, random_list):
    for i in random_list:
        empty.insert(i)
    for i in random_list:
        assert empty.delete(i) is True
        assert is_height_correct(empty) is True


def test_insert_huge_list(empty, random_list):
    for i in random_list:
        assert empty.insert(i) is True
        assert empty.root.color == BLACK
        assert is_height_correct(empty) is True


def test_search_huge_list(empty, random_list):
    for i in random_list:
        empty.insert(i)
    for i in random_list:
        assert empty.search(i) == i
