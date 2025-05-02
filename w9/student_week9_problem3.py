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
        '''=======Student's code======='''
    
    def addList(self, head2):
        '''=======Student's code======='''

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

if __name__ == '__main__':
    main()