class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.next = None

# TIP : None is considered as False in Python

class CircularLinkedList: # CircularLinked list class
    def __init__(self): # Initalize
        "Student Code"
    
    def insert(self, data):# Insert the node
        "Student Code"
    
    def delete(self): # Delete the node pointed by the cursor
        "Student Code"
    
    def move_next(self): # Move the cursor to the next node
        "Student Code"

    def search(self, data): # Search the node with specific value
        "Student Code"
    
    def display(self): # Display the linked list
        "Student Code"


circularLinkedList = CircularLinkedList()
circularLinkedList.insert(10)
circularLinkedList.insert(20)
circularLinkedList.insert(30)
circularLinkedList.display() # 10 -> 30 -> 20 -> (cursor)
circularLinkedList.move_next()
circularLinkedList.delete()
circularLinkedList.display() # 30 -> 10 -> (cursor)