class BSTNode:

    def __init__(self, key, parent=None, left=None, right=None):

        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BST:

    def __init__(self):
        self.root = None
        self.list = []

    def __str__(self):
        return str(self.key)

    def _find_iterative(self, node, key):
        current_node = node
        while current_node:

            if key == current_node.key:
                break

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node:
            return current_node
        else:
            raise KeyError("Key not found")

    def _preorder_generator(self, node):
        if node is None:
            return
        yield node.key
        if node.left is not None:
            yield from self._preorder_generator(node.left)
        if node.right is not None:
            yield from self._preorder_generator(node.right)

    def preorder(self):
        yield from self._preorder_generator(self.root)

    def _inorder_generator(self, node):
        if node is None:
            return
        if node.left is not None:
            yield from self._inorder_generator(node.left)
        yield node.key
        if node.right is not None:
            yield from self._inorder_generator(node.right)

    def inorder(self):
        yield from self._inorder_generator(self.root)

    def _postorder_generator(self, node):
        if node is None:
            return
        if node.left is not None:
            yield from self._postorder_generator(node.left)
        if node.right is not None:
            yield from self._postorder_generator(node.right)
        yield node.key

    def postorder(self):
        yield from self._postorder_generator(self.root)

    def _print_tree_indented(self, node, level=0):
        if node is None:
            return
        self._print_tree_indented(node.right, level+1)
        print ('  ' * level + str(node.key))
        self._print_tree_indented(node.left, level+1)

    def search(self, key):

        current_node = self._find_iterative(self.root, key)
        return key

    def insert(self, key):

        if self.root is None:
            self.root = BSTNode(key)
            return True

        current_node = self.root
        while current_node:

            if key == current_node.key:
                raise KeyError("They key already exists")

            elif key < current_node.key and current_node.left:
                current_node = current_node.left
            elif key > current_node.key and current_node.right:
                current_node = current_node.right
            else:
                break

        if key < current_node.key:
            current_node.left = BSTNode(key, current_node)
        else:
            current_node.right = BSTNode(key, current_node)
        return True

    def _replace_node(self, node, new_node):
        if node == self.root:
            self.root = new_node
            return

        parent = node.parent

        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            raise RuntimeError("Incorrect parent-children relation!")

    def _remove_node(self, node):
        if node.left and node.right:
            successor = node.right

            while successor.left:
                successor = successor.left

            node.key = successor.key
            self._remove_node(successor)

        elif node.left:
            self._replace_node(node, node.left)

        elif node.right:
            self._replace_node(node, node.right)

        else:
            self._replace_node(node, None)

    def delete(self, key):

        node = self._find_iterative(self.root, key)
        if node:
            self._remove_node(node)
            return True
