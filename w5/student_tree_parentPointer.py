class Node: # Tree Node class
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def setLeft(self, left):
        self.left = left
        if left is not None:
            left.parent = self
    
    def setRight(self, right):
        self.right = right
        if right is not None:
            right.parent = self

def is_leaf(root):
    return root.left is None and root.right is None

def height(position):
    if position is None:
        return -1
    if is_leaf(position):
        return 0
    else:
        height_left = height(position.left)
        height_right = height(position.right)
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

def is_root(node):
    return node.parent is None

def depth(node):
    if not node.parent:
        return 0
    return depth(node.parent) + 1
        

def main():
    # Create a binary tree
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7

    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(3))
    root.left.setLeft(Node(4))
    root.left.setRight(Node(5))
    root.right.setLeft(Node(6))
    root.right.setRight(Node(7))
    
    # Is leaf
    print(is_leaf(root)) # False
    print(is_leaf(root.left.left)) # True

    # Height of the tree
    print(height(root)) # 2
    print(height(root.right)) # 1
    print(height(root.right.right)) # 0

    # Is root
    print(is_root(root)) # True
    print(is_root(root.left)) # False

    # Depth of the node
    print(depth(root)) # 0
    print(depth(root.left)) # 1
    print(depth(root.left.left)) # 2
    


    
if __name__ == '__main__':
    main()