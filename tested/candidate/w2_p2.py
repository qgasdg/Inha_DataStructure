import array

"""
week2_problem2 에서 array를 순차적으로 채우지 않고
예를 들어, index가 2인곳 먼저 채우는 경우까지 고려한 DynamicArray
"""

class Node:
    def __init__(self, data=None):
        self.data = array.array('h', [0] * 3)
        self.next = None  # 다음 노드의 포인터

class DynamicArray:
    def __init__(self):
        self.capacity = 0  # 전체 노드에 저장 가능한 총 원소 개수 (노드 수 * 3)
        self.size = 0      # 현재 저장된 원소의 개수
        self.maxidx = 0
        self.prevmax = 0
        self.head = None   # 연결 리스트의 첫 번째 노드
        self.tail = None   # 연결 리스트의 마지막 노드

    def add(self, idx, item):
        """
        add(idx, item): 주어진 인덱스(idx) 위치에 item을 삽입하고,
        이후의 원소들을 한 칸씩 뒤로 밀어낸다.
        idx는 0 <= idx <= size 의 범위 내에 있다고 가정.
        """
        # 리스트가 비어 있는 경우: 첫 노드를 생성
        if self.head is None:
            self.capacity += 3       # 새 노드 하나당 3개의 원소 저장 가능
            self.size += 1           # 첫 원소 추가
            new_node = Node()
            self.head = new_node
            self.tail = new_node
            # 첫 노드의 배열에 idx 위치에 item을 저장 (일반적으로 idx는 0)
            new_node.data[idx] = item
            self.maxidx = idx
            return

        # 새 노드가 필요할 때
        if idx + 1 > self.capacity:
            self.capacity += 3
            new_node = Node()
            # 현재 tail 뒤에 새 노드를 연결하고 tail 갱신
            self.tail.next = new_node
            self.tail = new_node

        # 삽입할 위치(idx)에 해당하는 노드와 배열 내 오프셋을 찾는다.
        tmp = self.head
        i = 0
        # idx만큼 이동하며 적절한 노드와 배열 인덱스 결정
        for _ in range(idx):
            i += 1
            if i > 2:  # 한 노드 내 인덱스는 0~2 까지 존재하므로,
                i = 0
                tmp = tmp.next  # 다음 노드로 이동

        # targ: 원래 삽입 위치에 해당하는 노드 (나중에 이 위치에 새로운 item을 삽입할 예정)
        targ = tmp
        # 현재 위치의 값을 carry 변수에 저장 (이후 shift 연산 시 사용)
        carry = tmp.data[i]

        if carry == 0:
            tmp.data[i] = item
            self.size += 1  # 전체 원소 수 증가

            if idx > self.maxidx:
                self.prevmax = self.maxidx
                self.maxidx = idx
            return

        # idx부터 현재 size-1까지, 즉 삽입 위치부터 마지막 원소까지 한 칸씩 오른쪽으로 이동(shift)
        for _ in range(idx, self.maxidx + 1):
            # 현재 노드 내에서 i가 2보다 작으면 같은 노드 내에서 shift
            if i < 2:
                # 오른쪽으로 한 칸 이동: 현재 위치의 값은 carry로 덮어쓰고, 기존 값은 carry에 저장
                tmp.data[i + 1], carry = carry, tmp.data[i + 1]
                i += 1
            else:
                # 현재 노드의 마지막 위치(인덱스 2)까지 shift한 후,
                # 다음 노드로 넘어가서 그 노드의 첫 번째 원소와 shift 수행
                tmp = tmp.next
                tmp.data[0], carry = carry, tmp.data[0]
                i = 0
            if carry == 0:
                break

        # targ 노드의 idx 위치에 새 item을 삽입
        targ.data[idx % 3] = item
        self.size += 1  # 전체 원소 수 증가

        if idx > self.maxidx:
            self.prevmax = self.maxidx
            self.maxidx = idx
        else:
            self.maxidx += 1
        return

    def remove(self, idx):
        """
        remove(idx): 주어진 인덱스(idx)에 있는 원소를 제거하고,
        이후의 원소들을 한 칸씩 앞으로 당긴다.
        """
        # idx에 해당하는 노드와 배열 내 인덱스를 찾기 위해 front부터 탐색
        tmp = self.head
        i = 0
        for _ in range(idx):
            i += 1
            if i > 2:
                i = 0
                tmp = tmp.next

        # idx부터 마지막 원소까지, 한 칸씩 왼쪽으로 shift
        for _ in range(idx, self.maxidx + 1):
            if i < 2:
                # 같은 노드 내에서 왼쪽 shift: 현재 인덱스 i를 i+1의 값으로 덮어씀
                curr = tmp.data[i]
                tmp.data[i] = tmp.data[i + 1]
                i += 1
            else:
                # 현재 노드의 마지막 인덱스(2)에서는, 다음 노드의 첫 번째 원소를 가져와서 채운 후,
                # 다음 노드로 넘어가서 shift 진행
                curr = tmp.data[2]
                tmp.data[2] = tmp.next.data[0]
                tmp = tmp.next
                i = 0
            if curr == 0:
                break
        self.size -= 1  # 전체 원소 수 감소

        # 만약 제거 후 남은 원소의 개수가 정확히 capacity의 배수가 아니면, 마지막 노드가 비어있을 수 있음.
        if self.maxidx // 3 != self.prevmax // 3:
            self.capacity -= 3
            curr = self.head
            # 마지막 노드를 찾아 tail을 갱신 (마지막 노드는 curr.next가 None이 되어야 함)
            while curr.next:
                curr = curr.next
            self.tail = curr
            self.tail.next = None

        if idx == self.maxidx:
            self.maxidx = self.prevmax
        else:
            self.maxidx -= 1
        return

    def print(self):
        """
        print(): 현재 동적 배열에 저장된 모든 원소를 순서대로 출력.
        """
        tmp = self.head
        i = 0
        # 전체 원소 개수만큼 반복하면서 출력
        for _ in range(self.maxidx + 1):
            if i > 2:
                i = 0
                tmp = tmp.next
            print(tmp.data[i], end=' ')
            i += 1
        print()  # 줄바꿈
        return

def main():
    # 첫 번째 테스트: 10장의 카드(숫자)를 순차적으로 추가하고 출력
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
    arr_list.print()  # 예상 출력: 1 2 3 4 5 6 7 8 9 10

    # 두 번째 테스트: 인덱스 5 위치에 99 삽입
    arr_list.add(5, 99)
    arr_list.print()  # 예상 출력: 1 2 3 4 5 99 6 7 8 9 10

    # 세 번째 테스트: 인덱스 0의 원소 제거
    arr_list.remove(0)
    arr_list.print()  # 예상 출력: 2 3 4 5 99 6 7 8 9 10

    # 네 번째 테스트: 인덱스 9의 원소 제거
    arr_list.remove(9)
    arr_list.print()  # 예상 출력: 2 3 4 5 99 6 7 8 9

    # 다섯 번째 테스트: 인덱스 4의 원소 제거
    arr_list.remove(4)
    arr_list.print()  # 예상 출력: 2 3 4 5 6 7 8 9

    a = DynamicArray()
    a.add(2, 1)
    a.print() # 0 0 1
    a.add(3, 2)
    a.print() # 0 0 1 2
    a.remove(3)
    a.print() # 0 0 1
    a.add(1, 2)
    a.print() # 0 2 1

if __name__ == '__main__':
    main()
