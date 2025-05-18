import array
class HeapSort:
    def __init__(self, arr : array.array, n):
        self.capacity = n
        self.array = arr
        self.size = n
    
    def sort(self):
        self.build_heap()

        for i in range(self.size-1, 0, -1):
            temp = self.array[i]
            self.array[i] = self.array[0]
            self.array[0] = temp
            self.size -= 1
            self.downHeap(0)
    
    def build_heap(self):
        # DownHeap from the last non-leaf node to the root
        # Start from the last non-leaf, We can make all the subtrees heap
        # If we start from the root, children is not heap yet So, heap property is not guaranteed
        for i in range(self.size//2-1, -1, -1):
            self.downHeap(i)


    def downHeap(self, index):
        # Swap the current node with the smaller of its children if it is larger than either child
        if index >= self.size:
            return
        left = index * 2 + 1
        right = index * 2 + 2
        min_index = index
        if left < self.size and self.array[left] < self.array[min_index]:
            min_index = left
        if right < self.size and self.array[right] < self.array[min_index]:
            min_index = right
        if min_index != index:
            temp = self.array[index]
            self.array[index] = self.array[min_index]
            self.array[min_index] = temp
            self.downHeap(min_index)
    
    def print_array(self):
        for i in range(self.capacity):
            print(self.array[i], end=' ')
        print()
    
def main():
    arr = array.array('h', [1, 2, 3, 4, 5])
    heap_sort = HeapSort(arr, 5)
    print("Before sorting:")
    heap_sort.print_array()
    heap_sort.sort()
    print("After sorting:")
    heap_sort.print_array()

if __name__ == '__main__':
    main()