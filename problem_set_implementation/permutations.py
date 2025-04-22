import array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        ret = self.top.data
        self.top = self.top.next
        return ret
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def print(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()
        return

n = 3
stack = Stack()
visited = array.array('h', [0] * 10)
def permutations(num):
    if num == 0:
        stack.print()
        return
    for i in range(n, 0, -1):
        if visited[i]:
            continue
        visited[i] = True
        stack.push(i)
        permutations(num - 1)
        stack.pop()
        visited[i] = False
    return

if __name__ == "__main__":
    print(f"Permutations of {n}:")
    permutations(n)
