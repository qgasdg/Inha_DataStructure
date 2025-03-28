class Node: # Node class
    "Student Code"
# TIP : None is considered as False in Python

class LinkedList: # Linked list class
    def __init__(self): # Initalize
        "Student Code"
    
    def append(self, data): # Add new node at the end
        "Student Code"
    
    def prepend(self, data): # Add new node at the beginning
        "Student Code"
    
    def delete(self, data): # Delete the node with specific value
        "Student Code"
    
    def search(self, data): # Search the node with specific value
        "Student Code"
    
    def display(self): # Display the linked list
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')


linkedList = LinkedList()
linkedList.append(10)
linkedList.append(20)
linkedList.prepend(5)
linkedList.display() # 5 -> 10 -> 20 -> None
linkedList.delete(10)
linkedList.display() # 5 -> 20 -> None