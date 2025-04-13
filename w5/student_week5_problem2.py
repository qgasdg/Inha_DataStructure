class Node:
    def __init__(self, value):
        '''=======Student's code======='''

max_sum = 0

def maxPathSum(node):
    global max_sum
    '''=======Student's code======='''

def findMaxPathSum(root):
    global max_sum
    '''=======Student's code======='''

def main():
    #         1
    #       /   \
    #     -2     3
    #     / \   / \
    #    8  -1  4  -5


    root = Node(1)
    root.leftChild = Node(-2)
    root.rightChild = Node(3)
    root.leftChild.leftChild = Node(8)
    root.leftChild.rightChild = Node(-1)
    root.rightChild.leftChild = Node(4)
    root.rightChild.rightChild = Node(-5)

    print(findMaxPathSum(root))  
    
    
    # Output: 14 (1 + -2 + 3 + 4)

if __name__ == "__main__":
    main()