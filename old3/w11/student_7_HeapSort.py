import array


class HeapSort:
    def __init__(self, arr: array.array, n):
        self.capacity = n
        self.array = arr
        self.size = n

    def sort(self):
        """=======Student's code======="""
        self.build_heap()

    def build_heap(self):
        """=======Student's code======="""
        # 먼차이?
        for i in range(self.size - 1, -1, -1):
            self.downHeap(i)

    def downHeap(self, index):
        """=======Student's code======="""
        # 머하노
        if index >= self.size:
            return
        left, right = index * 2, index * 2 + 1
        if index == 0:
            left, right = 1, 2
        max_index = index
        if left < self.size and self.array[left] > self.array[index]:
            max_index = left
        if right < self.size and self.array[right] > self.array[index]:
            max_index = right
        if max_index != index:
            self.array[max_index], self.array[index] = (
                self.array[index],
                self.array[max_index],
            )
            self.downHeap(max_index)

    def print_array(self):
        for i in range(self.capacity):
            print(self.array[i], end=" ")
        print()


def main():
    arr = array.array("h", [1, 2, 3, 4, 5])
    heap_sort = HeapSort(arr, 5)
    print("Before sorting:")
    heap_sort.print_array()
    heap_sort.sort()
    print("After sorting:")
    heap_sort.print_array()


if __name__ == "__main__":
    main()
