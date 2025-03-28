class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: # Linked list class
    def __init__(self): # Initalize
        self.head = None
        self.tail = None
    
    def append(self, data): # Add new node at the end
        new_node = Node(data)

        # If there is no node in the linked list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        # Add new node at the tail
        self.tail.next = new_node
        self.tail = new_node

    def display(self): # Display the linked list
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def reverse_recursive(self, current, prev): 
        if not current:
            return prev
        nxt = current.next
        current.next = prev
        return self.reverse_recursive(nxt, current)

    def reverse(self):  # Reverse the linked list
        # If there is no node or only one node in the linked list
        if not self.head or self.head == self.tail:
            return

            # Change the head and the tail cause the head will be the tail after reversing
        self.tail = self.head
        self.head = self.reverse_recursive(self.head, None)

def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.display() # 1 -> 2 -> 3 -> 4 -> 5 -> None
    linked_list.reverse()
    linked_list.display() # 5 -> 4 -> 3 -> 2 -> 1 -> None
    linked_list.append(0)
    linked_list.display() # 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None

if __name__ == '__main__':
    main()