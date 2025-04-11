class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack: 
    def __init__(self): # Initalize
        self.head = None

    def push(self, data): # Add new node at the head
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def pop(self): # Delete the node at the head
        if not self.head:
            return None
        temp = self.head
        self.head = temp.next
        data = temp.data
        temp = None
        return data

    def peek(self): # Search the node at the head
        if not self.head:
            return None
        return self.head.data

    def print(self): # Print the data in the stack
        if not self.head:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()