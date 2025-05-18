import array
class HeapSort:
    def __init__(self, arr : array.array, n):
        self.capacity = n
        self.array = arr
        self.size = n
    
    def sort(self):
        '''=======Student's code======='''
    
    def build_heap(self):
        '''=======Student's code======='''


    def downHeap(self, index):
        '''=======Student's code======='''
    
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