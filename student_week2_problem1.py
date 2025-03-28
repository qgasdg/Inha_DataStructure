import array


# Node 클래스: 각 노드는 데이터를 저장하고 다음 노드를 가리키는 포인터를 가진다.
class Node:
    def __init__(self, data):
        self.data = data  # 노드에 저장할 데이터 (여기서는 이름 문자열)
        self.next = None  # 다음 노드에 대한 포인터


# NameList 클래스: 환형 연결 리스트를 구현하여 중복된 이름 제거 및 순서대로 출력하는 기능을 제공
class NameList:
    def __init__(self):
        # front: 연결 리스트의 시작 노드
        # back: 연결 리스트의 마지막 노드
        # cursor: 현재 삽입 위치를 위해 사용되는 임시 포인터 (보통 back을 사용)
        self.front = None
        self.back = None
        self.cursor = None

    def insert(self, data):
        # insert(data): 연결 리스트의 마지막에 새로운 데이터를 삽입하는 메소드.
        # 새 노드를 만들고, 이를 환형 연결 리스트에 추가한다.

        # 삽입 전에 cursor를 현재 마지막 노드(back)로 지정
        self.cursor = self.back

        # 새 노드 생성
        new_node = Node(data)

        # 만약 리스트가 비어 있다면(즉, cursor가 None이면)
        if not self.cursor:
            # 새 노드가 front, back, cursor 모두가 됨.
            self.cursor = new_node
            self.front = new_node
            self.back = new_node
            # 단일 노드의 경우, 자신의 다음 노드로 자신을 가리켜 환형 구조를 유지
            self.cursor.next = self.cursor
            return

        # 일반적인 경우: 새 노드를 cursor(현재 back)의 뒤에 삽입한다.
        # 새 노드의 next는 cursor의 next(즉, front)를 가리킴
        new_node.next = self.cursor.next
        # cursor의 next를 새 노드로 연결 (즉, 뒤에 새 노드 삽입)
        self.cursor.next = new_node

        # 만약 cursor가 리스트의 마지막 노드였다면, 새 노드가 새로운 마지막 노드가 된다.
        if self.cursor == self.back:
            self.back = self.cursor.next
        return

    def removeDuplicates(self):
        # removeDuplicates(): 연결 리스트 내 중복된 이름을 제거하는 메소드.
        # 최초 등장한 순서를 유지하며, 이후에 등장하는 중복 요소들은 모두 제거한다.

        if not self.front:
            return  # 리스트가 비어 있다면 아무 작업도 하지 않음

        # x: 기준이 되는 노드 (각 노드의 데이터와 리스트 내 다른 모든 노드를 비교)
        x = self.front
        while True:
            prev = x  # prev: 비교 도중 현재 순회 중인 노드의 이전 노드
            it = x.next  # it: x 다음 노드부터 한 바퀴 돌아가면서 비교
            # x 기준으로 한 바퀴 순회하면서 x.data와 동일한 데이터를 가진 노드를 제거
            while it != self.front:
                if it.data == x.data:
                    # 중복 발견: prev.next를 it.next로 연결하여 it를 리스트에서 제거
                    prev.next = it.next
                    # it를 업데이트 (삭제한 후, prev의 다음 노드가 새로운 it)
                    it = prev.next
                else:
                    # 중복이 아니면, prev와 it를 한 칸씩 이동
                    prev = it
                    it = it.next
            # x를 다음 노드로 이동하여, 리스트 내 모든 노드에 대해 중복 제거 수행
            x = x.next
            # 한 바퀴 돌면(다시 front에 도달하면) 중복 제거 작업 종료
            if x == self.front:
                break
        return

    def display(self):
        # display(): 연결 리스트의 모든 데이터를 순서대로 출력하는 메소드.
        if not self.cursor:
            print("empty")
            return
        # front 노드의 데이터를 출력
        print(self.front.data, end=' ')
        tmp = self.front.next
        # front를 다시 만날 때까지(환형 연결 리스트이므로) 순회하며 출력
        while tmp != self.front:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()  # 줄바꿈
        return


def main():
    # 첫 번째 테스트: 중복된 이름이 포함된 리스트
    name_list1 = NameList()
    name_list1.insert("지혜")
    name_list1.insert("민수")
    name_list1.insert("유나")
    name_list1.insert("민수")
    name_list1.insert("태훈")
    name_list1.insert("유나")
    name_list1.display()  # 예상 출력: 지혜 민수 유나 민수 태훈 유나
    name_list1.removeDuplicates()
    name_list1.display()  # 예상 출력: 지혜 민수 유나 태훈

    # 두 번째 테스트: 모든 이름이 같은 리스트
    name_list3 = NameList()
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.insert("수빈")
    name_list3.display()  # 예상 출력: 수빈 수빈 수빈 수빈
    name_list3.removeDuplicates()
    name_list3.display()  # 예상 출력: 수빈


if __name__ == '__main__':
    main()
