import pytest
import random
from algorithms.binary_search_tree import BSTNode, BST
from algorithms.red_black_tree import RBNode, RBTree, RED, BLACK
from algorithms.singly_list import Node, UnorderedList


@pytest.fixture(scope="function")
def empty_list():
    empty_list = []
    return empty_list


@pytest.fixture(scope="function")
def one_list():
    one_list = [1]
    return one_list


@pytest.fixture(scope="function")
def sorted_list():
    sorted_list = list(range(1000))
    return sorted_list


@pytest.fixture(scope="function")
def reverse_sorted():
    reverse_sorted = list(range(1000, 0, -1))
    return reverse_sorted


@pytest.fixture(scope="function")
def random_list():
    random_list = random.sample(range(0, 1000), 1000)
    return random_list


@pytest.fixture(scope="function")
def empty_BST():
    empty_BST = BST()
    return empty_BST


@pytest.fixture(scope="function")
def parent_BST():
    parent_BST = BST()
    parent_BST.root = BSTNode(5, None, None, None)
    return parent_BST


@pytest.fixture(scope="function")
def parent_left_BST():
    parent_left_BST = BST()
    parent_left_BST.root = BSTNode(5, None, None, None)
    parent_left_BST.root.left = BSTNode(3, None, None, None)
    parent_left_BST.root.left.parent = parent_left_BST.root
    return parent_left_BST


@pytest.fixture(scope="function")
def parent_right_BST():
    parent_right_BST = BST()
    parent_right_BST.root = BSTNode(5, None, None, None)
    parent_right_BST.root.right = BSTNode(7, None, None, None)
    parent_right_BST.root.right.parent = parent_right_BST.root
    return parent_right_BST


@pytest.fixture(scope="function")
def parent_both_BST():
    parent_both_BST = BST()
    parent_both_BST.root = BSTNode(5, None, None, None)
    parent_both_BST.root.left = BSTNode(3, None, None, None)
    parent_both_BST.root.left.parent = parent_both_BST.root
    parent_both_BST.root.right = BSTNode(7, None, None, None)
    parent_both_BST.root.right.parent = parent_both_BST.root
    return parent_both_BST


@pytest.fixture(scope="function")
def empty():
    empty = RBTree()
    return empty


@pytest.fixture(scope="function")
def one():
    one = RBTree()
    one.root = RBNode(5, BLACK)
    one.root.p = one.sentinel
    one.root.left = one.sentinel
    one.root.right = one.sentinel
    return one


@pytest.fixture(scope="function")
def five_right():
    five_right = RBTree()
    five_right.root = RBNode(3, BLACK)
    five_right.root.p = five_right.sentinel
    five_right.root.right = RBNode(5, BLACK)
    five_right.root.right.p = five_right.root
    five_right.root.left = RBNode(2, BLACK)
    five_right.root.left.p = five_right.root
    five_right.root.left.right = five_right.sentinel
    five_right.root.left.left = five_right.sentinel
    five_right.root.right.right = RBNode(7, RED)
    five_right.root.right.right.p = five_right.root.right
    five_right.root.right.right.right = five_right.sentinel
    five_right.root.right.right.left = five_right.sentinel
    five_right.root.right.left = RBNode(4, RED)
    five_right.root.right.left.p = five_right.root.right
    five_right.root.right.left.right = five_right.sentinel
    five_right.root.right.left.left = five_right.sentinel
    return five_right


@pytest.fixture(scope="function")
def five_left():
    five_left = RBTree()
    five_left.root = RBNode(5, BLACK)
    five_left.root.p = five_left.sentinel
    five_left.root.right = RBNode(7, BLACK)
    five_left.root.right.p = five_left.root
    five_left.root.right.right = five_left.sentinel
    five_left.root.right.left = five_left.sentinel
    five_left.root.left = RBNode(3, BLACK)
    five_left.root.left.p = five_left.root
    five_left.root.left.right = RBNode(4, RED)
    five_left.root.left.right.p = five_left.root.left
    five_left.root.left.right.right = five_left.sentinel
    five_left.root.left.right.left = five_left.sentinel
    five_left.root.left.left = RBNode(2, RED)
    five_left.root.left.left.p = five_left.root.left
    five_left.root.left.left.right = five_left.sentinel
    five_left.root.left.left.left = five_left.sentinel
    return five_left


@pytest.fixture(scope="function")
def nodes1():
    nodes1 = [10, 15, 7, 8, 5, 6]
    return nodes1


@pytest.fixture(scope="function")
def nodes2():
    nodes2 = [10, 9, 13, 11, 15, 12]
    return nodes2


@pytest.fixture(scope="function")
def empty_singly():
    empty_singly = UnorderedList()
    return empty_singly


@pytest.fixture(scope="function")
def two_elements():
    two_elements = UnorderedList()
    two_elements._head = Node(1)
    two_elements._head.next = Node(2)
    two_elements._length = 2
    two_elements._tail = Node(2)
    return two_elements
