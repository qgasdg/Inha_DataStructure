class Node: # Tree Node class
    def __init__(self, data):
        '''=======Student's code======='''

    def setLeft(self, left):
        '''=======Student's code======='''
    
    def setRight(self, right):
        '''=======Student's code======='''

    def is_leaf(root):
        '''=======Student's code======='''
    
def InorderTraversal(root): # Left, Root, Right
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

    # Inorder Traversal
    InorderTraversal(root) # 4 2 5 1 6 3 7
    print()

if __name__ == '__main__':
    main()