class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NameList:
    def __init__(self):
        self.front = None
        self.back = None
        self.cursor = None

    def insert(self, data):
        self.cursor = self.back
        new_node = Node(data)
        if not self.cursor:
            self.cursor = new_node
            self.front = new_node
            self.back = new_node
            self.cursor.next = self.cursor
            return

        new_node.next = self.cursor.next
        self.cursor.next = new_node
        if self.cursor == self.back:
            self.back = self.cursor.next
        return

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
        return

    def display(self):
        if not self.cursor:
            print("empty")
            return
        print(self.front.data, end=' ')
        tmp = self.front.next
        while tmp != self.front:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()
        return

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