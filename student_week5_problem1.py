import array

class Node:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

    def is_leaf(self):
        return (self.leftChild == None and self.rightChild == None)


def boundaryTraversal(root):
    temp_boundary = root

    while not temp_boundary.is_leaf():
        print(temp_boundary.data,end=' ')
        temp_boundary = temp_boundary.leftChild

    InorderLeafTraversal(root)

    temp_boundary = root.rightChild
    while not temp_boundary.is_leaf():
        print(temp_boundary.data,end=' ')
        temp_boundary = temp_boundary.rightChild


def InorderLeafTraversal(root):
    if root.is_leaf():
        print(root.data,end=' ')
    
    if root.leftChild != None:
        InorderLeafTraversal(root.leftChild)
    if root.rightChild != None:
        InorderLeafTraversal(root.rightChild)

    
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

    boundaryTraversal(root) # 20 8 4 10 14 25 22

if __name__ == "__main__":
    main()
=======
import array

class Node:
    def __init__(self, value):
        '''=======Student's code======='''

'''=======Student's code======='''


def boundaryTraversal(root):
    '''=======Student's code======='''
    
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

    boundaryTraversal(root) # 20 8 4 10 14 25 22

if __name__ == "__main__":
    main()
