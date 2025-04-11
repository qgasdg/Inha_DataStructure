import array

class Stack:
    def __init__(self, n):
        self.capacity = n
        self.size = 0
        self.array = array.array('h', [0] * n)
    
    def push(self, item):
        self.array[self.size] = item
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        ret = self.array[self.size - 1]
        self.array[self.size - 1] = 0
        self.size -= 1
        return ret

    def is_empty(self):
        return self.size == 0
    
class Queue:
    def __init__(self, n):
        self.Stack1 = Stack(n)
        self.Stack2 = Stack(n)
    
    def enqueue(self, item):
        self.Stack1.push(item)
        return
    
    def dequeue(self):
        while not self.Stack1.is_empty():
            self.Stack2.push(self.Stack1.pop())
        if self.Stack2.is_empty():
            return None
        ret = self.Stack2.pop()
        while not self.Stack2.is_empty():
            self.Stack1.push(self.Stack2.pop())
        return ret
    
    def is_empty(self):
        return self.Stack1.is_empty()


def main():
    stack = Stack(2)
    print(stack.is_empty())  # True
    stack.push(1)
    stack.push(2)
    print(stack.is_empty())  # False
    for i in range(3):
        print(stack.pop(), end= ' ') # 2 1 None
    print()

    queue = Queue(2)
    print(queue.is_empty())  # True
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.is_empty())  # False
    for i in range(3):
        print(queue.dequeue(), end= ' ') # 1 2 None
    print()


if __name__ == '__main__':
    main()