import array

class Heap():
    def __init__(self, arr, n):
        self.capacity = n + 1
        self.array = array.array('h', [0] + arr)
        self.size = n

    def build_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.downHeap(i)

    def downHeap(self, index):
        if index >= self.size:
            return

        left = index * 2
        right = index * 2 + 1
        max_index = index

        if left <= self.size and self.array[left] > self.array[max_index]:
            max_index = left
        if right <= self.size and self.array[right] > self.array[max_index]:
            max_index = right
        if max_index != index:
            self.array[0] = self.array[index]
            self.array[index] = self.array[max_index]
            self.array[max_index] = self.array[0]
            self.downHeap(max_index)
    
    def remove_max(self):
        if self.size < 1:
            return None

        max_value = self.array[1]
        self.array[1] = self.array[self.size]
        self.size -= 1
        self.downHeap(1)
        return max_value

def main():
    n = 5
    arr = [1, 2, 3, 4, 5]

    heap = Heap(arr, n)
    heap.build_heap()

    for _ in range(n): # 5 4 3 2 1
        print(heap.remove_max(), end = ' ')
    print()

if __name__ == '__main__':
    main()