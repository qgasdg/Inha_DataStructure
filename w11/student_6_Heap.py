import array

class Heap:
    def __init__(self, n):
        '''=======Student's code======='''
    
    def insert(self, item):
        '''=======Student's code======='''
    
    def upHeap(self, index):
        '''=======Student's code======='''

    def remove_min(self):
        '''=======Student's code======='''
    
    def downHeap(self, index):
        '''=======Student's code======='''

def main():
    heap = Heap(5+1)
    heap.insert(5)
    heap.insert(4)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    for i in range(6):
        print(heap.remove_min(), end= ' ') # 1 2 3 4 5 None
    print()

if __name__ == '__main__':
    main()