from array import array


class RBTree:
    # Constants for node colors
    RED = 0
    BLACK = 1

    class Node:
        def __init__(self, key):
            self.key = key
            self.color = RBTree.RED
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.NIL = self.Node(None)
        self.NIL.color = self.BLACK
        self.root = self.NIL
        self.size = 0
        # Using array.array to store the keys
        self.keys = array("i")  # 'i' for signed integers

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = self.Node(key)
        node.left = self.NIL
        node.right = self.NIL

        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self.keys.append(key)
        self.size += 1
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == self.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == self.RED:
                    u.color = self.BLACK
                    k.parent.color = self.BLACK
                    k.parent.parent.color = self.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = self.BLACK
                    k.parent.parent.color = self.RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == self.RED:
                    u.color = self.BLACK
                    k.parent.color = self.BLACK
                    k.parent.parent.color = self.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = self.BLACK
                    k.parent.parent.color = self.RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = self.BLACK

    def search(self, key):
        node = self.root
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node if node != self.NIL else None

    def inorder_traversal(self):
        def _inorder(node):
            if node != self.NIL:
                _inorder(node.left)
                print(
                    f"({node.key}, {'RED' if node.color == self.RED else 'BLACK'})",
                    end=" ",
                )
                _inorder(node.right)

        _inorder(self.root)
        print()
