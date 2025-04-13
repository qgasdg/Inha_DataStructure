class Node:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

    def is_leaf(self):
        return self.leftChild is None and self.rightChild is None

def InorderLeafTraversal(root):
    if root.is_leaf():
        print(root.data, end=' ')
        return
    if root.leftChild is not None:
        InorderLeafTraversal(root.leftChild)
    if root.rightChild is not None:
        InorderLeafTraversal(root.rightChild)
    return

def rightChildTraversal(root):
    if root.is_leaf():
        return
    rightChildTraversal(root.rightChild)
    print(root.data, end=' ')
    return

def boundaryTraversal(root):
    temp_boundary = root

    while not temp_boundary.is_leaf():
        print(temp_boundary.data, end=' ')
        temp_boundary = temp_boundary.leftChild

    InorderLeafTraversal(root)

    temp_boundary = root.rightChild
    rightChildTraversal(temp_boundary)
    print()
    return

def main():
    #        20
    #       /  \
    #      8    22
    #     / \     \
    #    4   12    25
    #       /  \
    #      10   14
    root = Node(20)
    root.leftChild = Node(8)
    root.rightChild = Node(22)
    root.leftChild.leftChild = Node(4)
    root.leftChild.rightChild = Node(12)
    root.leftChild.rightChild.leftChild = Node(10)
    root.leftChild.rightChild.rightChild = Node(14)
    root.rightChild.rightChild = Node(25)

    boundaryTraversal(root)  # 20 8 4 10 14 25 22

    #        20
    #       /  \
    #      8    22
    #     / \     \
    #    4   12    25
    #       /  \    \
    #      10   14   23

    root.rightChild.rightChild.rightChild = Node(23)

    boundaryTraversal(root)  # 20 8 4 10 14 23 25 22

if __name__ == "__main__":
    main()
