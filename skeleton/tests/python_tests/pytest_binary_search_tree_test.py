from pytest import raises


def test_search_empty_BST(empty_BST):
    raises(KeyError, "empty_BST.search(7)")


def test_search_found_parent_BST(parent_BST):
    assert parent_BST.search(5) == parent_BST.root.key


def test_search_not_found_parent_BST(parent_BST):
    with raises(KeyError):
        parent_BST.search(7)


def test_search_found_both_BST(parent_both_BST):
    assert parent_both_BST.search(3) == parent_both_BST.root.left.key


def test_insert_empty_BST(empty_BST):
    assert empty_BST.insert(5) is True
    assert empty_BST.root.key == 5


def test_insert_right_parent_BST(parent_BST):
    assert parent_BST.insert(7) is True
    assert parent_BST.root.right.key == 7


def test_insert_left_parent_BST(parent_BST):
    assert parent_BST.insert(3) is True
    assert parent_BST.root.left.key == 3


def test_delete_empty_BST(empty_BST):
    with raises(KeyError):
        empty_BST.delete(7)


def test_delete_parent_BST(parent_BST):
    assert parent_BST.delete(5) is True
    assert parent_BST.root is None


def test_delete_leaf_parent_both_BST(parent_both_BST):
    assert parent_both_BST.delete(7) is True
    assert parent_both_BST.root.right is None


def test_delete_leaf_parent_both_BST_not_found(parent_both_BST):
    with raises(KeyError):
        parent_both_BST.delete(8)


def test_delete_node_only_right_child_parent_right_BST(parent_right_BST):
    assert parent_right_BST.delete(5) is True
    assert parent_right_BST.root.key == 7


def test_delete_node_only_left_child_parent_left_BST(parent_left_BST):
    assert parent_left_BST.delete(5) is True
    assert parent_left_BST.root.key == 3


def test_delete_node_both_children_parent_both_BST(parent_both_BST):
    assert parent_both_BST.delete(5) is True
    assert parent_both_BST.root.key == 7


def test_preorder_not_empty(parent_both_BST):
    assert parent_both_BST.root.key == list(parent_both_BST.preorder())[0]
    assert parent_both_BST.root.left.key == list(parent_both_BST.preorder())[1]
    assert parent_both_BST.root.right.key == list(parent_both_BST.preorder())[2]
    assert len(list(parent_both_BST.preorder())) == 3


def test_inorder_not_empty(parent_both_BST):
    assert parent_both_BST.root.key == list(parent_both_BST.inorder())[1]
    assert parent_both_BST.root.left.key == list(parent_both_BST.inorder())[0]
    assert parent_both_BST.root.right.key == list(parent_both_BST.inorder())[2]
    assert len(list(parent_both_BST.inorder())) == 3


def test_inorder_not_empty(parent_both_BST):
    assert parent_both_BST.root.key == list(parent_both_BST.postorder())[2]
    assert parent_both_BST.root.left.key == list(parent_both_BST.postorder())[0]
    assert parent_both_BST.root.right.key == list(parent_both_BST.postorder())[1]
    assert len(list(parent_both_BST.postorder())) == 3


def test_preorder_empty(empty_BST):
    assert len(list(empty_BST.preorder())) == 0


def test_inorder_empty(empty_BST):
    assert len(list(empty_BST.inorder())) == 0


def test_postorder_empty(empty_BST):
    assert len(list(empty_BST.postorder())) == 0


def test_delete_huge_list(random_list, empty_BST):
    for i in random_list:
        empty_BST.insert(i)
    for i in random_list:
        assert empty_BST.delete(i) is True
    assert len(list(empty_BST.inorder())) == 0


def test_insert_huge_list(random_list, empty_BST):
    for i in random_list:
        assert empty_BST.insert(i) is True


def test_search_huge_list(random_list, empty_BST):
    for i in random_list:
        empty_BST.insert(i)
    for i in random_list:
        assert empty_BST.search(i) == i
