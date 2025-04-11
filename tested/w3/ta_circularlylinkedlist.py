class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.next = None

# TIP : None is considered as False in Python

class CircularLinkedList: # CircularLinked list class
    def __init__(self): # Initalize
        self.front = None
        self.back = None
        self.cursor = None # 커서라는 개념의 등장
    
    def insert(self, data):# Insert the node
        new_node = Node(data)

        # If there is no node in the linked list
        if not self.cursor:
            self.front = new_node
            self.back = new_node
            self.cursor = new_node
            self.cursor.next = self.cursor # Pointing itself for circular linked list
            return
        
        new_node.next = self.cursor.next
        self.cursor.next = new_node

        # If new node is inserted at the back
        if self.cursor == self.back:
            self.back = new_node
    
    def delete(self): # Delete the node pointed by the cursor
        # If there is no node in the linked list
        if not self.cursor:
            return
        
        # If the node to delete is the only node in the linked list
        if self.cursor == self.front and self.cursor == self.back:
            self.front = None
            self.back = None
            self.cursor = None
            return
        
        temp = self.cursor.next
        if temp == self.front:
            self.front = temp.next
        if temp == self.back:
            self.back = self.cursor
        self.cursor.next = temp.next
    
    def move_next(self): # Move the cursor to the next node
        if self.cursor:
            self.cursor = self.cursor.next

    def search(self, data): # Search the node with specific value
        # If there is no node in the linked list
        if not self.cursor:
            return False
        
        temp = self.cursor
        while True:
            if temp.data == data:
                return True
            temp = temp.next
            # If the cursor has checked all the nodes
            if temp == self.cursor:
                return False
    
    def display(self): # Display the linked list
        # If there is no node in the linked list
        if not self.cursor:
            print('List is empty')
            return
        
        temp = self.cursor
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            # If the cursor has checked all the nodes
            if temp == self.cursor:
                break
        print('(cursor)')


circularLinkedList = CircularLinkedList()
circularLinkedList.insert(10)
circularLinkedList.insert(20)
circularLinkedList.insert(30)
circularLinkedList.display() # 10 -> 30 -> 20 -> (cursor)
circularLinkedList.move_next()
circularLinkedList.delete()
circularLinkedList.display() # 30 -> 10 -> (cursor)