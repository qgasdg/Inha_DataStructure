import array

class Node:
    def __init__(self):
        self.array = array.array('h', [0] * 3)
        self.next = None

class DynamicArray:
    def __init__(self):
        self.head = None
        self.tail = None
        self.capacity = None

    def add(self, idx, data):
        if not self.head:
            if idx > 2:
                print("index out of range")
                return

            new_node = Node()
            new_node.array[idx] = data

            self.head = new_node
            self.tail = new_node

            return

        tmp = self.head
        end = 2
        while end < idx:
            if not tmp.next:
                new_node = Node()
                new_node.array[idx % 3] = data
                self.tail.next = new_node
                self.tail = new_node
                return
            tmp = tmp.next
            end += 3

        tmp.array[idx % 3] = data
        return

    def remove(self, idx):
        if not self.head:
            print("index out of range")
            return

        tmp = self.head
        end = 2
        while end < idx:
            tmp = tmp.next
            end += 3

        for i in range(idx % 3, 2):
            tmp.array[i] = tmp.array[i + 1]

        prev = tmp
        tmp = tmp.next
        while tmp:
            prev.array[2] = tmp.array[0]
            for i in range(1, 3):
                tmp.array[i - 1] = tmp.array[i]
            prev = tmp
            tmp = tmp.next
        return

    def show(self):
        tmp = self.head
        while tmp:
            for i in range(3):
                print(tmp.array[i], end=' ')
            tmp = tmp.next
        print()
        return

arr = DynamicArray()
arr.add(0, 1)
arr.add(1, 2)
arr.add(2, 3)
arr.add(3, 4)
arr.add(4, 5)
arr.show()