class Node:
    def __init__(self, value):
        self.value = value
        self.childrenHead = None
        self.childrenTail = None
        self.next = None
    
    def addChild(self, value):
        child = Node(value)
        if not self.childrenHead:
            self.childrenHead = child
            self.childrenTail = child
        else:
            self.childrenTail.next = child
            self.childrenTail = child

def preOrderTraversal(root): # root, child1, child2, ...
    if not root:
        return
    print(root.value, end=' ')
    child = root.childrenHead
    while child:
        preOrderTraversal(child)
        child = child.next

def postOrderTraversal(root): # child1, child2, ..., root
    if not root:
        return
    child = root.childrenHead
    while child:
        postOrderTraversal(child)
        child = child.next
    print(root.value, end=' ')

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