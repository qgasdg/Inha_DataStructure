class Node:
    def __init__(self, data):
        '''=======Student's code======='''


def is_leaf(root):
    '''=======Student's code======='''


def height(position):
    '''=======Student's code======='''

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