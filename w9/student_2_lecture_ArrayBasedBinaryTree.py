import array

class Tree:
    def __init__(self, n, rootValue): # Initialize the tree with the given capacity
        '''=======Student's code======='''

    def setLeftChild(self, parentIndex, childValue):
        '''=======Student's code======='''
    
    def setRightChild(self, parentIndex, childValue):
       '''=======Student's code======='''
        
    def getValue(self, index):
        '''=======Student's code======='''
    
    def getLeftChild(self, index):
        '''=======Student's code======='''
    
    def getRightChild(self, index):
        '''=======Student's code======='''

    def getParent(self, index):
        '''=======Student's code======='''
    
def main():
    # Create a binary tree
    #         7
    #        / \
    #       6   5
    #      / \ / \
    #     4  3 2  1
    tree = Tree(100, 7)
    tree.setLeftChild(1, 6)
    tree.setRightChild(1, 5)
    tree.setLeftChild(2, 4)
    tree.setRightChild(2, 3)
    tree.setLeftChild(3, 2)
    tree.setRightChild(3, 1)

    print(tree.getLeftChild(1)) # 6
    print(tree.getRightChild(1)) # 5
    print(tree.getParent(2)) # 7
    print(tree.getLeftChild(2)) # 4
    print(tree.getRightChild(2)) # 3

if __name__ == "__main__":
    main()
