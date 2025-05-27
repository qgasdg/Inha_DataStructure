import array

class Node: # Tree Node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Sorter:
    def __init__(self, arr : array.array, n):
        self.array = arr
        self.root = None
        self.size = n
        self.index = 0

    def printArray(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def binaryTree(self):
        self.root = Node(self.array[0])
        for i in range(1, self.size):
            cursor = self.root
            while True:
                if self.array[i] < cursor.data:
                    if cursor.left is None:
                        cursor.left = Node(self.array[i])
                        break
                    else:
                        cursor = cursor.left
                else:
                    if cursor.right is None:
                        cursor.right = Node(self.array[i])
                        break
                    else:
                        cursor = cursor.right
    
    def sort(self):
        self.binaryTree()
        self.index = 0
        self.treeSort(self.root)
        

    def treeSort(self, node):
        if node is None:
            return
        self.treeSort(node.left)
        self.array[self.index] = node.data
        self.index += 1
        self.treeSort(node.right)

def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6])
    sorter = Sorter(arr, n)
    sorter.printArray()
    sorter.sort()
    sorter.printArray()

if __name__ == "__main__":
    main()