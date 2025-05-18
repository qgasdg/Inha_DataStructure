class Node: # Tree Node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_leaf(root): # Check if the node is a leaf node
    return root.left is None and root.right is None

def height(position): # Calculate the height of the tree
    if position is None: # Check if the node is None
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


def main():
    # Create a binary tree
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Is leaf
    print(is_leaf(root)) # False
    print(is_leaf(root.left.left)) # True

    # Height of the tree
    print(height(root)) # 2
    print(height(root.right)) # 1
    print(height(root.right.right)) # 0

    
if __name__ == '__main__':
    main()