import array

class Stack:
    def __init__(self, n): 
        self.capacity = n
        self.stack = array.array('h', [0] * n)
        self.top = -1
    
    def push(self, item): 
        if self.is_full():
            print("Stack is full")
            return
        self.top += 1
        self.stack[self.top] = item
        return

    def pop(self): 
        if self.is_empty():
            print("Stack is empty")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item
        
    def top(self): 
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]
        
    def print(self): 
        if self.is_empty():
            print("Stack is empty")
            return
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=' ')
        print()
        return
        
    def is_empty(self): 
        return self.top == -1

    def is_full(self): 
        return self.top == self.capacity - 1

