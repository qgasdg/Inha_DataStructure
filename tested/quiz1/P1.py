class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.next = None

class NameList:
    def __init__(self): 
        self.front = None
        self.back = None
        self.cursor = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.cursor is None:
            self.front = new_node
            self.back = new_node
            self.cursor = new_node
            new_node.next = new_node
            return
        self.back.next = new_node
        new_node.next = self.front
        self.back = new_node
        return
    
    def removeDuplicates(self):
        if self.cursor is None:
            return
        self.cursor = self.front
        while True:
            it = self.cursor.next
            prev = self.cursor
            while it != self.front:
                if it.data == self.cursor.data:
                    prev.next = it.next
                    if it is self.back:
                        self.back = prev
                    it = it.next
                    continue
                prev = it
                it = it.next
            self.cursor = self.cursor.next
            if self.cursor == self.front:
                break
        return
    
    def display(self):
        if self.cursor is None:
            return 
        self.cursor = self.front
        while True:
            print(self.cursor.data, end=' ')
            self.cursor = self.cursor.next
            if self.cursor == self.front:
                break
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
    name_list1.display() # 지혜 민수 유나 민수 태훈 유나
    name_list1.removeDuplicates()
    name_list1.display() # 지혜 민수 유나 태훈

    name_list3 = NameList()
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.display() # 수빈 수빈 수빈 수빈
    name_list3.removeDuplicates()
    name_list3.display() # 수빈

if __name__ == '__main__':
    main()