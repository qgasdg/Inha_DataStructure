import array

class Node:
    def __init__(self):
        # Each node stores an array of three integers (of type 'h') and a pointer to the next node.
        self.data = array.array('h', [0] * 3)
        self.next = None

class DynamicArray:
    def __init__(self):
        # 초기에는 동적 배열이 비어있으므로, front와 back 포인터를 None으로 설정하고,
        # 전체 저장된 요소의 개수를 나타내는 length를 0으로 초기화한다.
        # Initially, the dynamic array is empty.
        self.front = None
        self.back = None
        self.length = 0

    def add(self, idx, item):
        # add(idx, item): idx 위치에 item을 삽입하고, 이후 요소들을 오른쪽으로 한 칸씩 이동시킨다.
        # (Assume idx is in the range 0 <= idx <= self.length.)
        if idx < 0 or idx > self.length:
            return  # 혹은 예외 발생

        # If the list is empty, create the first node.
        if self.front is None:
            new_node = Node()
            new_node.data[0] = item
            self.front = new_node
            self.back = new_node
            self.length = 1
            return

        # Determine which node and the offset inside that node correspond to the index.
        node_index = idx // 3
        offset = idx % 3

        # Traverse to the node at position node_index.
        current = self.front
        for i in range(node_index):
            current = current.next

        # Determine how many items are stored in this node.
        # All nodes except the last hold 3 items.
        if current != self.back:
            count = 3
        else:
            # In the last node, the count is self.length % 3 (if nonzero), else full (3) if length > 0.
            r = self.length % 3
            count = r if r != 0 else 3

        # If current node is not full, insert the item here.
        if count < 3:
            # Shift elements right within current node from index 'offset' to 'count-1'.
            for i in range(count, offset, -1):
                current.data[i] = current.data[i - 1]
            current.data[offset] = item
            self.length += 1
        else:
            # The node is full, so we need to insert by carrying over the bumped elements.
            # (Insertion causes a cascade shift across subsequent nodes.)
            carry = item
            cur = current
            pos = offset
            while True:
                # In a full node (count == 3), save the last element to become carry.
                bumped = cur.data[2]
                # Shift right the elements from index 'pos' up to index 2.
                for i in range(2, pos, -1):
                    cur.data[i] = cur.data[i - 1]
                cur.data[pos] = carry
                carry = bumped
                # Set insertion position to 0 in the next node.
                pos = 0
                if cur == self.back:
                    # If we are at the last node, allocate a new node and insert the carry.
                    new_node = Node()
                    new_node.data[0] = carry
                    new_node.next = self.front
                    self.back.next = new_node
                    self.back = new_node
                    break
                else:
                    cur = cur.next
            self.length += 1

    def remove(self, idx):
        # remove(idx): idx 위치의 요소를 제거하고, 이후 요소들을 한 칸씩 왼쪽으로 이동시킨다.
        if idx < 0 or idx >= self.length:
            return  # 혹은 예외 발생

        node_index = idx // 3
        offset = idx % 3
        current = self.front
        for i in range(node_index):
            current = current.next

        # Determine count in current node.
        if current != self.back:
            count = 3
        else:
            r = self.length % 3
            count = r if r != 0 else 3

        # In current node, shift left from the removal offset.
        for i in range(offset, count - 1):
            current.data[i] = current.data[i + 1]
        # Propagate the shift across subsequent nodes.
        cur = current
        while cur != self.back:
            nxt = cur.next
            # Bring the first element of nxt into the last position of cur.
            cur.data[2] = nxt.data[0]
            # Shift left the data in nxt.
            for i in range(0, 2):
                nxt.data[i] = nxt.data[i + 1]
            cur = nxt
        # Now, adjust the last node's count.
        # For the last node, the count becomes:
        if self.back == self.front:
            r = self.length % 3
            count_last = r if r != 0 else 3
        else:
            r = self.length % 3
            count_last = r if r != 0 else 3

        # If the last node becomes empty (i.e., count_last was 1 before removal), and it is not the only node, remove it.
        if count_last == 1:
            if self.back == self.front:
                self.front = None
                self.back = None
            else:
                # Find the node before the last node.
                temp = self.front
                while temp.next != self.back:
                    temp = temp.next
                temp.next = self.front
                self.back = temp
        self.length -= 1

    def print(self):
        # show(): Print all elements in order.
        if self.front is None:
            print("empty")
            return
        result = []
        current = self.front
        while True:
            # For nodes other than the last, all 3 positions are valid.
            if current != self.back:
                for i in range(3):
                    result.append(str(current.data[i]))
            else:
                # For the last node, the count is self.length % 3 (if nonzero), else 3 if list is non-empty.
                r = self.length % 3
                count = r if r != 0 else 3
                for i in range(count):
                    result.append(str(current.data[i]))
                break
            current = current.next
            if current == self.front:
                break
        print(" ".join(result))


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
    arr_list.print()  # Expected output: 1 2 3 4 5 6 7 8 9 10

    arr_list.add(5, 99)
    arr_list.print()  # Expected output: 1 2 3 4 5 99 6 7 8 9 10

    arr_list.remove(0)
    arr_list.print()  # Expected output: 2 3 4 5 99 6 7 8 9 10

    arr_list.remove(9)
    arr_list.print()  # Expected output: 2 3 4 5 99 6 7 8 9

    arr_list.remove(4)
    arr_list.print()  # Expected output: 2 3 4 5 6 7 8 9


if __name__ == '__main__':
    main()
