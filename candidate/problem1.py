class Node:
    def __init__(self, data):
        # Node stores data and a pointer to the next node.
        self.data = data
        self.next = None

class NameList:
    def __init__(self):
        # In a circular linked list, if front is None, the list is empty.
        # Managing a back pointer helps with efficient insertions.
        self.front = None
        self.back = None

    def insert(self, data):
        new_node = Node(data)
        if self.front is None:
            # If the list is empty, the new node becomes front and back,
            # and points to itself.
            self.front = new_node
            self.back = new_node
            new_node.next = new_node
        else:
            # Insert the new node after the back and update the back pointer.
            new_node.next = self.front
            self.back.next = new_node
            self.back = new_node

    def removeDuplicates(self):
        if not self.front:
            return

        x = self.front
        while True:
            prev = x
            it = x.next
            # x 기준으로 한 바퀴 돌면서 중복 제거
            while it != self.front:
                if it.data == x.data:
                    # 중복이면 삭제: prev는 그대로두고 it를 건너뛰기
                    prev.next = it.next
                    it = prev.next
                else:
                    prev = it
                    it = it.next
            x = x.next
            if x == self.front:
                break

    def display(self):
        if self.front is None:
            print("empty")
            return
        result = []
        current = self.front
        result.append(current.data)
        current = current.next
        while current != self.front:
            result.append(current.data)
            current = current.next
        print(" ".join(result))

def main():
    name_list1 = NameList()
    name_list1.insert("지혜")
    name_list1.insert("민수")
    name_list1.insert("유나")
    name_list1.insert("민수")
    name_list1.insert("태훈")
    name_list1.insert("유나")
    name_list1.display()  # Expected: 지혜 민수 유나 민수 태훈 유나
    name_list1.removeDuplicates()
    name_list1.display()  # Expected: 지혜 민수 유나 태훈

    name_list3 = NameList()
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.display()  # Expected: 수빈 수빈 수빈 수빈
    name_list3.removeDuplicates()
    name_list3.display()  # Expected: 수빈

if __name__ == '__main__':
    main()