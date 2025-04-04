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
