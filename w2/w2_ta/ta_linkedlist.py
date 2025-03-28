class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.link = None

# TIP : None is considered as False in Python

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
        self.tail.link = new_node
        self.tail = new_node

    def prepend(self, data): # Add new node at the beginning
        new_node = Node(data)

        # Add new node at the head
        new_node.link = self.head
        self.head = new_node

        # If there is no node in the linked list
        if not self.tail:
            self.tail = new_node    
    
    def delete(self, data): # Delete the node with specific value
        temp = self.head

        # Check if the head is the node to delete
        if temp and temp.data == data:
            self.head = temp.link
            if self.head is None:
                self.tail = None
            temp = None
            return
        
        # Check if the node is in the middle or the tail
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.link
        
        if temp is None:
            return
        
        # Delete the node
        prev.link = temp.link
        if temp == self.tail:
            self.tail = prev
        temp = None
    
    def search(self, data): # Search the node with specific value
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.link
        return False
    
    def display(self): # Display the linked list
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.link
        print('None')

    def reverse(self):  # Reverse the linked list
        # If there is no node or only one node in the linked list
        if not self.head or self.head == self.tail:
            return

            # Reverse the linked list
        prev = None
        current = self.head #current = 5
        while current:
            linked_node = current.link # 처음에 헤드랑 연결된 곳이 linked_node(20)
            current.link = prev # 20이란 값을 previous로 설정해줌.
            prev = current # 5를 previous로 설정해줌.
            current = linked_node # 20을 current로 설정해줌.

        # Change the head and the tail
        temp = self.head
        self.head = self.tail
        self.tail = temp















linkedList = LinkedList()
linkedList.append(10)
linkedList.append(20)
linkedList.prepend(5)
linkedList.append(23)
linkedList.append(64)
linkedList.append(12)
linkedList.display() # 5 -> 10 -> 20 -> None
linkedList.delete(10)
linkedList.display() # 5 -> 20 -> None
linkedList.reverse()
linkedList.display() # 5 -> 20 -> None
