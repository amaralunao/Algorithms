from pytest import raises


def test_len_empty(empty_singly):
    assert empty_singly.__len__() == 0


def test_len_two_elements(two_elements):
    assert two_elements.__len__() == 2


def test_is_empty_empty(empty_singly):
    assert empty_singly.is_empty() is True


def test_is_empty_two_elements(two_elements):
    assert two_elements.is_empty() is False


def test__get_index_empty(empty_singly):
    with raises(IndexError):
        empty_singly._get_index(0)


def test__get_index_handled_two_elements(two_elements):
    assert two_elements._get_index(1) == (two_elements._head,
                                          two_elements._head.next)


def test__get_index_unhandled_two_elements(two_elements):
    with raises(IndexError):
        two_elements._get_index(3)


def test__getitem__empty(empty_singly):
    with raises(IndexError):
        empty_singly.__getitem__(0)


def test__getitem__handled_two_elements(two_elements):
    assert two_elements.__getitem__(1) == (two_elements._tail.data)


def test__getitem__unhandled_two_elements(two_elements):
    with raises(IndexError):
        two_elements.__getitem__(3)


def test__setitem__empty(empty_singly):
    with raises(IndexError):
        empty_singly.__setitem__(0, 10)


def test__getitem__handled_two_elements(two_elements):
    two_elements[0] = 10
    assert two_elements._head.data == 10


def test__getitem__unhandled_two_elements(two_elements):
    with raises(IndexError):
        two_elements.__setitem__(3, 10)


def test__search_empty(empty_singly):
    with raises(ValueError):
        empty_singly._search()


def test__search_found_two_elements(two_elements):
    assert two_elements._search(2) == (two_elements._head,
                                       two_elements._head.next)


def test__search_not_found_two_elements(two_elements):
    with raises(ValueError):
        two_elements._search(3)


def test_push_empty(empty_singly):
    empty_singly.push(3)
    assert empty_singly._head.data == 3
    assert empty_singly.__len__() == 1


def test_push_two_elements(two_elements):
    two_elements.push(3)
    assert two_elements._head.data == 3
    assert two_elements.__len__() == 3


def test_remove_empty(empty_singly):
    with raises(ValueError):
        empty_singly.remove(0)


def test_remove_found_two_elements(two_elements):
    two_elements.remove(2)
    assert two_elements._head.next is None
    assert two_elements.__len__() == 1


def test_remove_not_found_two_elements(two_elements):
    with raises(ValueError):
        two_elements.remove(3)


def test_pop_empty(empty_singly):
    with raises(IndexError):
        empty_singly.pop(3)


def test_pop_handled_two_elements(two_elements):
    assert two_elements.pop(0) == 1
    assert two_elements._head.next is None
    assert two_elements.__len__() == 1


def test_pop_indexNone_two_elements(two_elements):
    assert two_elements.pop() == 2
    assert two_elements._head.next is None
    assert two_elements.__len__() == 1


def test_pop_unhandled_two_elements(two_elements):
    with raises(IndexError):
        two_elements.pop(3)


def test_append_empty(empty_singly):
    empty_singly.append(1)
    assert empty_singly._head.data == 1
    assert empty_singly.__len__() == 1


def test_append_two_elements(two_elements):
    two_elements.append(3)
    assert two_elements._tail.data == 3
    assert two_elements.__len__() == 3


def test_insert_handled_empty(empty_singly):
    empty_singly.insert(0, 3)
    assert empty_singly._head.data == 3
    assert empty_singly.__len__() == 1


def test_insert_unhandled_empty(empty_singly):
    with raises(IndexError):
        empty_singly.insert(1, 3)


def test_insert_handled_two_elements(two_elements):
    two_elements.insert(1, 3)
    assert two_elements._head.next.data == 3
    assert two_elements.__len__() == 3


def test_insert_unhandled_two_elements(two_elements):
    with raises(IndexError):
        two_elements.insert(2, 3)
