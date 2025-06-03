import array


class Heap:
    def __init__(self, n):
        """=======Student's code======="""
        self.capacity = n
        self.array = array.array("h", [0] * n)
        self.size = 1

    def insert(self, item):
        """=======Student's code======="""
        if self.size < self.capacity:
            self.array[self.size] = item
            self.upHeap(self.size)
            self.size += 1

    def upHeap(self, index):
        """=======Student's code======="""
        if index <= 1:
            return
        parent = index // 2
        if self.array[index] < self.array[parent]:
            self.array[0] = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = self.array[0]
            # self.array[index], self.array[parent] = self.array[parent], self.array[index]
            self.upHeap(parent)

    def remove_min(self):
        """=======Student's code======="""
        if self.size > 1:
            value = self.array[1]
            self.array[1] = self.array[self.size - 1]
            self.size -= 1
            self.downHeap(1)
            return value
        else:
            return None

    def downHeap(self, index):
        """=======Student's code======="""
        if index >= self.size:
            return
        left, right = index * 2, index * 2 + 1
        min_index = index
        if left < self.size and self.array[left] < self.array[index]:
            min_index = left
        if right < self.size and self.array[right] < self.array[index]:
            min_index = right
        # 둘 다 작다면 right로 감
        # left로 가고싶으면? if문 순서 바꾼다
        if min_index != index:
            self.array[0] = self.array[index]
            self.array[index] = self.array[min_index]
            self.array[min_index] = self.array[0]
            self.downHeap(min_index)


def main():
    heap = Heap(5 + 1)
    heap.insert(5)
    heap.insert(4)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    for i in range(6):
        print(heap.remove_min(), end=" ")  # 1 2 3 4 5 None
    print()


if __name__ == "__main__":
    main()
