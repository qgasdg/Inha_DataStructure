class Node:
    def __init__(self, value):
        self.value = value
        self.childrenHead = None
        self.childrenTail = None
        self.next = None

    def addChild(self, value):
        new_node = Node(value)
        if self.childrenHead is None:
            self.childrenHead = new_node
            self.childrenTail = new_node
            return
        self.childrenTail.next = new_node
        self.childrenTail = new_node
        """ # not using tail
        tmp = self.childrenHead
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node
        self.childrenTail = new_node
        return
        """

def preOrderTraversal(root): 
    if root:
        print(root.value, end=' ')
        tmp = root.childrenHead
        while tmp:
            preOrderTraversal(tmp)
            tmp = tmp.next

def postOrderTraversal(root):
    if root:
        tmp = root.childrenHead
        while tmp:
            postOrderTraversal(tmp)
            tmp = tmp.next
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