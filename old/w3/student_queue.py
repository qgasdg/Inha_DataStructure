import array

class Queue:
    def __init__(self, n): 
        '''=======Student's code======='''
        self.size = n
        self.queue = array.array('i', [0] * n)

    def enqueue(self, item): 
        '''=======Student's code======='''
        if self.is_full():
            raise OverflowError("Queue is full")
        else:
            self.queue.append(item)

    def dequeue(self): 
        '''=======Student's code======='''
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.queue.pop(0)

    def peek(self): 
        '''=======Student's code======='''
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.queue[0]
        
    def print(self): 
        '''=======Student's code======='''
        for i in range(len(self.queue)):
            print(self.queue[i], end=' ')
        print()
        
    def is_empty(self): 
        '''=======Student's code======='''
        return len(self.queue) == 0
        
    def is_full(self): 
        '''=======Student's code======='''
        return len(self.queue) == self.size
