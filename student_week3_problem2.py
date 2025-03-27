import array

class Queue:
    def __init__(self):
        # Fixed-size array of 1001 short integers
        self.data = array.array('h', [0] * 1001)
        self.front = 0
        self.rear = 0
        self.capacity = 1001

    def enqueue(self, item):
        # Optionally, check if the queue is full
        next_rear = (self.rear + 1) % self.capacity
        if next_rear == self.front:
            raise IndexError("Queue is full")
        self.data[self.rear] = item
        self.rear = next_rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        return item

    def is_empty(self):
        return self.front == self.rear
        
class CardGame:
    def __init__(self):
        self.cards = Queue()
        
    def lastCard(self, n):
        for i in range(1, n + 1):
            self.cards.enqueue(i)
        ret = None
        while not self.cards.is_empty():
            ret = self.cards.dequeue()
            if self.cards.is_empty():
                break
            self.cards.enqueue(self.cards.dequeue())
        return ret

def main():
    cardGame = CardGame()
    print(cardGame.lastCard(1))
    print(cardGame.lastCard(4))
    print(cardGame.lastCard(7))
    print(cardGame.lastCard(1000))

if __name__ == "__main__":
    main()
        