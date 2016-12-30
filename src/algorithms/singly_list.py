
import io


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class UnorderedList:

    def __init__(self):
        self._head = self._tail = None
        self._length = 0

    def __str__(self):

        if self._length == 0:
            return '[]'

        current = self._head
        string_list = io.StringIO()
        string_list.write('[')

        while current is not None:

            string_list.write(current.__str__())
            if current.next is not None:
                string_list.write(', ')
            else:
                string_list.write(']')
            current = current.next

        return string_list.getvalue()

    def __len__(self):
        return self._length

    def _get_index(self, index=None):
        if index in range(self._length):

            previous = None
            current = self._head
            count = 0

            while current is not None and count != index:
                previous = current
                current = current.next
                count += 1
            return previous, current
        else:
            raise IndexError

    def __getitem__(self, index):
        previous, current = self._get_index(index)
        return current.data

    def __setitem__(self, index, item):
        previous, current = self._get_index(index)
        current.data = item
        return

    def is_empty(self):
        return self._head is None and self._tail is None


    def _search(self, item=None):
        current = self._head
        previous = None
        count = 0
        while current is not None and count != self._length:
            if current.data == item:
                return previous, current
            else:
                previous = current
                current = current.next
                count += 1
        raise ValueError

    def push(self, item):
        temp = Node(item)
        if self._head is None and self._tail is None:
            temp.next = self._head = self._tail
            self._head = self._tail = temp
        else:
            temp.next = self._head
            self._head = temp
        self._length += 1

    def _remove_method(self, previous, current):
        if previous is None:
            self._head = current.next
            self._length -= 1
            if current.next is None:
                self._tail = None
        else:
            previous.next = current.next
            self._length -= 1
            if previous.next is None:
                self._tail = previous

    def remove(self, item):
        previous, current = self._search(item)
        self._remove_method(previous, current)

    def pop(self, index=None):
        if index is None:
            previous, current = self._get_index(self._length - 1)
        else:
            previous, current = self._get_index(index)
        self._remove_method(previous, current)
        return current.data

    def append(self, item):
        temp = Node(item)
        if self._head is None:
            self._head = self._tail = temp
        else:
            self._tail.next = temp
            self._tail = temp
        self._length += 1

    def insert(self, index, item):

        if index == 0:
            self = self.push(item)
        elif index not in range(self._length):
            raise IndexError
        else:
            current = self._head
            count = 0

            while current.next is not None and count < index - 1:
                current = current.next
                count += 1

            temp = Node(item)
            temp.next = current.next
            current.next = temp
            self._length += 1

'''
mylist = UnorderedList()

mylist.push(31)
mylist.push(77)
mylist.push(17)
mylist.push(93)
mylist.push(26)
mylist.push(54)
mylist.append(3)
mylist.__str__()
print(mylist.pop())
mylist.__str__()
print(mylist._tail.data)
#print(mylist._get_index(3))
#mylist.insert(4, 66)
mylist[3]
print(len(mylist))
mylist[3] = 10
mylist.__str__()
'''
