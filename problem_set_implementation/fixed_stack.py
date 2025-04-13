import array


class Stack:
    def __init__(self, n):
        self.array = array.array('h', [0] * n)
        self.capacity = n
        self.size = 0 # push는 size에 pop은 size - 1에

    def push(self, item):
        if self.size == self.capacity:
            print(Exception('Stack is FULL'))
            return
        self.array[self.size] = item
        self.size += 1

    def pop(self): # 지운 data는 없앨까? 그대로 둘까?
        if self.size == 0:
            print(Exception('Stack is EMPTY'))
            return
        self.size -= 1
        ret = self.array[self.size]
        self.array[self.size] = 0
        return ret

    def top(self):
        if self.size == 0:
            print(Exception('Stack is EMPTY'))
            return
        return self.array[self.size - 1]

    def print(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
        return

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

if __name__ == '__main__':
    stack = Stack(2)
    stack.push(1)
    stack.push(2)
    stack.push(3) # Stack is FULL
    print(stack.is_full()) # True
    print(stack.pop()) # 2
    print(stack.pop()) # 1
    print(stack.pop()) # Stack is EMPTY & Return None
    print(stack.is_empty()) # True