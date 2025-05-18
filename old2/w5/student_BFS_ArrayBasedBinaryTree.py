import array

'''=======Student's code======='''

class Tree:
    def __init__(self, n, rootValue):
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
    
    def BFS(self):
        '''=======Student's code======='''
    

def main():
    # Create a binary tree
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7

    tree = Tree(100, 1)
    tree.setLeftChild(1, 2)
    tree.setRightChild(1, 3)
    tree.setLeftChild(2, 4)
    tree.setRightChild(2, 5)
    tree.setLeftChild(3, 6)
    tree.setRightChild(3, 7)

    # Perform BFS traversal
    tree.BFS() # Output: 1 2 3 4 5 6 7

if __name__ == "__main__":
    main()