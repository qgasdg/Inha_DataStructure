class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


class MergeLinkedList:
    def __init__(self):
        self.head = None

    def addList(self, head2):
        if head2 is None:               # 빈 리스트면 끝
            return
        if self.head is None:           # 첫 번째 입력
            self.head = head2
            return

        dummy = Node(0)                 # << 핵심: 더미 노드
        tail = dummy
        p1, p2 = self.head, head2

        while p1 and p2:                # 두 리스트를 병합
            if p1.data <= p2.data:
                tail.next, p1 = p1, p1.next
            else:
                tail.next, p2 = p2, p2.next
            tail = tail.next

        tail.next = p1 or p2            # 남은 쪽 전부 연결
        self.head = dummy.next          # 새 머리 갱신


def main():
    # Create two linked lists
    # List 1: 1 -> 3 -> 5
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)

    # List 2: 2 -> 4 -> 6
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)

    # Print the original lists
    print("List 1: ", end='')
    print_linkedList(head1)
    print("List 2: ", end='')
    print_linkedList(head2)

    # Merge the lists
    merged_list = MergeLinkedList()
    merged_list.addList(head1)
    merged_list.addList(head2)

    # Print the merged list
    print("Merged List: ", end='')
    print_linkedList(merged_list.head)

    # -- TestCase2 --
    """
    1 -> 2 -> 3 -> 4 -> 5 : head1 소진
    5 -> 6 -> 6 : 나머지 head2를 전부 잘 연결할 수 있는가?
    """

    # Create two linked lists
    # List 1: 1 -> 3 -> 5
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)

    # List 2: 2 -> 4 -> 6 -> 6
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)
    head2.next.next.next = Node(6)

    # Print the original lists
    print("List 1: ", end='')
    print_linkedList(head1) # 1 3 5
    print("List 2: ", end='')
    print_linkedList(head2) # 2 4 6 6

    # Merge the lists
    merged_list = MergeLinkedList()
    merged_list.addList(head1)
    merged_list.addList(head2)

    # Print the merged list
    print("Merged List: ", end='')
    print_linkedList(merged_list.head) # 1 2 3 4 5 6 6

if __name__ == '__main__':
    main()
