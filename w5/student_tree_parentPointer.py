class Node: # Tree Node class
    def __init__(self, data):
        '''=======Student's code======='''

    def setLeft(self, left):
        '''=======Student's code======='''
    
    def setRight(self, right):
        '''=======Student's code======='''

def is_leaf(root):
    '''=======Student's code======='''

def height(position):
    '''=======Student's code======='''

def is_root(node):
    '''=======Student's code======='''

def depth(node):
    '''=======Student's code======='''
        

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