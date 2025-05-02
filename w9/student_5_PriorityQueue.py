import array

class PriorityQueue:
    def __init__(self, n): # Initialize the queue with the given capacity
        """=======Student's code======="""
        self.capacity = n
        self.array = array.array('h', [0] * self.capacity)
        self.front = 0
        self.back = 0
        self.size = 0

    def add(self, item): # Push the item to the queue and sort it
        """=======Student's code======="""
        """O(N)"""
        """근데 front, back 없이 거꾸로 구현하면 똑같이 가능!"""
        if self.size == self.capacity:
            return -1
        self.array[self.back] = item
        for offset in range(self.size, 0, -1):
            front = (self.front + offset - 1) % self.capacity
            back = (self.front + offset) % self.capacity
            if self.array[front] > self.array[back]:
                self.array[front], self.array[back] = self.array[back], self.array[front]
            else:
                break
        self.size += 1
        self.back = (self.back + 1) % self.capacity
        return
    
    def remove_min(self):
        """=======Student's code======="""
        """O(1)"""
        """근데 front, back 없이 거꾸로 구현하면 똑같이 가능!"""
        if self.size == 0:
            return None
        ret = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return ret

def main():
    queue = PriorityQueue(5)
    queue.add(5)
    queue.add(4)
    queue.add(3)
    queue.add(2)
    queue.add(1)
    for i in range(6):
        print(queue.remove_min(), end= ' ') # 1 2 3 4 5 None
    print()

if __name__ == '__main__':
    main()