import array

'''=======Student's code=======(you can use data structure from previous lectures)'''
class Queue:
    def __init__(self, n):
        self.capacity = n
        self.array = array.array('h', [0] * self.capacity)
        self.front = 0
        self.back = 0

    def enqueue(self, value):
        self.array[self.back] = value
        self.back = (self.back + 1) % self.capacity

    def dequeue(self):
        ret = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        return ret

    def empty(self):
        return self.front == self.back

class Tree:
    def __init__(self, n, rootValue): # Initialize the tree with the given capacity
        """=======Student's code=======(copy and paste from previous code)"""
        self.capacity = n
        self.array = array.array('h', [0] * self.capacity)
        self.array[1] = rootValue

    def setLeftChild(self, parentIndex, childValue):
        """=======Student's code=======(copy and paste from previous code)"""
        if parentIndex * 2 >= self.capacity or parentIndex < 1:
            return
        self.array[parentIndex * 2] = childValue
    
    def setRightChild(self, parentIndex, childValue):
        """=======Student's code=======(copy and paste from previous code)"""
        if parentIndex * 2 + 1 >= self.capacity or parentIndex < 1:
            return
        self.array[parentIndex * 2 + 1] = childValue
        
    def getValue(self, index):
        """=======Student's code=======(copy and paste from previous code)"""
        if index < 1 or index >= self.capacity:
            return None
        return self.array[index]
    
    def getLeftChild(self, index):
        """=======Student's code=======(copy and paste from previous code)"""
        if index * 2 >= self.capacity or index < 1:
            return None
        return self.array[index * 2]
    
    def getRightChild(self, index):
        """=======Student's code=======(copy and paste from previous code)"""
        if index * 2 + 1 >= self.capacity or index < 1:
            return None
        return self.array[index * 2 + 1]

    def getParent(self, index):
        """=======Student's code=======(copy and paste from previous code)"""
        if index <= 1 or index >= self.capacity:
            return None
        return self.array[index // 2]
    
    def BFS(self):
        """=======Student's code=======(copy and paste from previous code)"""
        q = Queue(self.capacity)
        q.enqueue(1)
        while not q.empty():
            tmp = q.dequeue()
            print(self.array[tmp], end=' ')
            left, right = tmp * 2, tmp * 2 + 1
            if self.getLeftChild(tmp) != 0:
                q.enqueue(left)
            if self.getRightChild(tmp) != 0:
                q.enqueue(right)
        print()
        """의심해라"""
        """겸손해라"""

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