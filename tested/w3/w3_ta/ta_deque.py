import array

class Deque:
    def __init__(self, n): # Initialize the deque with the given capacity
        self.capacity = n
        self.array = array.array('h', [0]*self.capacity)
        self.size = 0
        self.front = 0
        self.rear = 0

    def insert_front(self, item): # Put the item to the front of the deque
        if self.size < self.capacity:
            self.front = (self.front-1) % self.capacity
            self.array[self.front] = item
            self.size += 1

    def insert_rear(self, item): # Put the item to the rear of the deque
        if self.size < self.capacity:
            self.array[self.rear] = item
            self.rear = (self.rear+1) % self.capacity
            self.size += 1

    def pop_front(self): # Get the item from the front of the deque
        if self.size > 0:
            data = self.array[self.front]
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            return data
        else:
            return None

    def pop_rear(self): # Get the item from the rear of the deque
        if self.size > 0:
            self.rear = (self.rear-1) % self.capacity
            self.size -= 1
            return self.array[self.rear]
        else:
            return None

    def peek_front(self): # Return the front item of the deque
        if self.size > 0:
            return self.array[self.front]
        else:
            return None

    def peek_rear(self): # Return the rear item of the deque
        if self.size > 0:
            return self.array[(self.rear-1) % self.capacity]
        else:
            return None

    def print(self): # Print all the items in the deque from front to rear
        idx = self.front
        for i in range(self.size):
            print(self.array[idx], end=' ')
            idx = (idx+1) % self.capacity
        print()

    def is_empty(self): # Check if the deque is empty
        return self.size == 0

    def is_full(self): # Check if the deque is full
        return self.size == self.capacity