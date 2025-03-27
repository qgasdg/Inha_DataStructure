import array


class Node:
    def __init__(self):
        self.data = array.array('h', [0] * 3)
        self.next = None


class DynamicArray:
    def __init__(self):
        self.capacity = 0
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, idx, item):
        if not self.head:
            self.capacity += 3
            self.size += 1
            new_node = Node()
            self.head = new_node
            self.tail = new_node
            new_node.data[idx] = item
            return

        if self.size == self.capacity:
            self.capacity += 3
            new_node = Node()
            self.tail.next = new_node
            self.tail = new_node

        tmp = self.head
        i = 0
        for _ in range(idx):
            i += 1
            if i > 2:
                i = 0
                tmp = tmp.next

        targ = tmp
        carry = tmp.data[i]

        # Now loop over how many times you need to shift
        for _ in range(idx, self.size):
            # SHIFT LOGIC, updating i each time
            if i < 2:
                # shift within the same node
                tmp.data[i + 1], carry = carry, tmp.data[i + 1]
                i += 1
            else:
                tmp = tmp.next
                tmp.data[0], carry = carry, tmp.data[0]
                i = 0
        targ.data[idx % 3] = item
        self.size += 1
        return

    def remove(self, idx):
        tmp = self.head
        i = 0
        for _ in range(idx):
            i += 1
            if i > 2:
                i = 0
                tmp = tmp.next

        for _ in range(idx, self.size):
            if i < 2:
                tmp.data[i] = tmp.data[i + 1]
                i += 1
                # print(i)
                # print(*tmp.data)
            else:
                tmp.data[2] = tmp.next.data[0]
                # print(*tmp.data)
                tmp = tmp.next
                i = 0

        self.size -= 1
        if self.size % 3 == 0:
            self.capacity -= 3
            curr = self.head
            while curr.next:
                curr = curr.next
            self.tail = curr
            self.tail.next = None

    def print(self):
        tmp = self.head
        i = 0
        for _ in range(self.size):
            if i > 2:
                i = 0
                tmp = tmp.next
            print(tmp.data[i], end=' ')
            i += 1
        print()

def main():
    arr_list = DynamicArray()

    arr_list.add(0, 1)
    arr_list.add(1, 2)
    arr_list.add(2, 3)
    arr_list.add(3, 4)
    arr_list.add(4, 5)
    arr_list.add(5, 6)
    arr_list.add(6, 7)
    arr_list.add(7, 8)
    arr_list.add(8, 9)
    arr_list.add(9, 10)
    arr_list.print()  # 1 2 3 4 5 6 7 8 9 10

    arr_list.add(5, 99)
    arr_list.print()  # 1 2 3 4 5 99 6 7 8 9 10

    arr_list.remove(0)
    arr_list.print()  # 2 3 4 5 99 6 7 8 9 10

    arr_list.remove(9)
    arr_list.print()  # 2 3 4 5 99 6 7 8 9

    arr_list.remove(4)
    arr_list.print()  # 2 3 4 5 6 7 8 9


if __name__ == '__main__':
    main()