from TreeMap import TreeMap

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 1

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    # positional-based utility methods
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    # override balancing hooks
    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)

    def _rebalance_access(self, p):
        self._rebalance(p)

    def _relink(self, parent, child, make_left_child: bool):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)): # single rotation
            self._rotate(y)
            return y
        else: # double rotation
            self._rotate(x)
            self._rotate(x)
            return x


def main():
    avl = AVLTreeMap()

    # 삽입
    avl[10] = 'ten'
    avl[20] = 'twenty'
    avl[5] = 'five'
    avl[15] = 'fifteen'

    # 조회
    print(avl[10])  # 'ten'
    print(avl[5])  # 'five'

    # 존재하지 않는 키 조회 시 KeyError
    # print(avl[100])  # KeyError 발생

    # 삭제
    del avl[10]

    # 키 순서대로 출력 (in-order traversal)
    for key in avl:
        print(key, avl[key])

if __name__ == '__main__':
    main()