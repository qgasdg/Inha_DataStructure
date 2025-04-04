class Node:
    def __init__(self, value):
        '''=======Student's code======='''
    
    def addChild(self, value):
        '''=======Student's code======='''

def preOrderTraversal(root): 
    '''=======Student's code======='''

def postOrderTraversal(root):
    '''=======Student's code======='''

def main():
    # Create a tree
    #            1
    #        /   |    \
    #       2    3     4
    #      /|\  / \   / \
    #     5 6 7 8  9 10  11


    root = Node(1)
    root.addChild(2)
    root.addChild(3)
    root.addChild(4)
    root.childrenHead.addChild(5)
    root.childrenHead.addChild(6)
    root.childrenHead.addChild(7)
    root.childrenHead.next.addChild(8)
    root.childrenHead.next.addChild(9)
    root.childrenTail.addChild(10)
    root.childrenTail.addChild(11)

    # Print the tree in pre-order
    preOrderTraversal(root) # 1 2 5 6 7 3 8 9 4 10 11
    print()
    # Print the tree in post-order
    postOrderTraversal(root) # 5 6 7 2 8 9 3 10 11 4 1

if __name__ == "__main__":
    main()