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
        """=======Student's code======="""
        self.head = None

    def addList(self, head2):
        """=======Student's code======="""
        if head2 is None:
            return
        if self.head is None:
            self.head = head2
            return

        if self.head.data <= head2.data:
            min_head = self.head
            cur = self.head.next
            cur2 = head2
        else:
            min_head = head2
            cur = self.head
            cur2 = head2.next

        tmp = min_head

        while cur and cur2:
            if cur.data <= cur2.data:
                tmp.next = cur
                cur = cur.next
            else:
                tmp.next = cur2
                cur2 = cur2.next
            tmp = tmp.next

        # Attach any remaining element
        if cur:
            tmp.next = cur
        else:
            tmp.next = cur2

        self.head = min_head


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
