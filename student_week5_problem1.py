import array

class Node:
    def __init__(self, value):
        '''=======Student's code======='''
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
def isLeaf(node):
    '''=======Student's code======='''
    return node.leftChild is None and node.rightChild is None

class Stack:
    def __init__(self, n):
        '''=======Student's code======='''
        self.array = array.array('h', [0] * n)
        self.capacity = n
        self.size = 0
        
    def push(self, item):
        '''=======Student's code======='''
        if self.size == self.capacity:
            return
        self.array[self.size] = item
        self.size += 1

    def pop(self):
        '''=======Student's code======='''
        if self.size == 0:
            return
        self.size -= 1
        return self.array[self.size]
        
    def is_empty(self):
        '''=======Student's code======='''
        return self.size == 0
        
def printLeaves(node):
    '''=======Student's code======='''
    if node is None:
        return
    if isLeaf(node):
        print(node.value, end=' ')
        return
    printLeaves(node.leftChild)
    printLeaves(node.rightChild)
    
def boundaryTraversal(root):
    '''=======Student's code======='''
    if root is None:
        return
    tmp = root
    while tmp.leftChild:
        print(tmp.value, end=' ')
        tmp = tmp.leftChild
    # 위는 왼쪽 boundary
    printLeaves(root) # 리프 바운더리
    # 아래는 오른쪽 바운더
    TREEHEIGHT = 100
    RCs = Stack(TREEHEIGHT)
    tmp = root.rightChild
    while tmp:
        if isLeaf(tmp):
            break
        RCs.push(tmp.value)
        tmp = tmp.rightChild
    while not RCs.is_empty():
        print(RCs.pop(), end=' ')
    print()
    
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
    
    #     1
    #    /
    #   2
    #  / \
    # 4   5
    #      \
    #       7
    r = Node(1)
    r.leftChild = Node(2)
    r.leftChild.leftChild = Node(4)
    r.leftChild.rightChild = Node(5)
    r.leftChild.rightChild.rightChild = Node(7)
    
    boundaryTraversal(r) 
    """
    1 2 4 7 -> 이게 맞는듯
    1 2 4 7 5
    """
    
if __name__ == "__main__":
    main()
