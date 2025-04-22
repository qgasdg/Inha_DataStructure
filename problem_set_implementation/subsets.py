class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
    
    def is_empty(self):
        return self.head is None

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

num = 3
st = Stack()

def subsetsByStack(n):
    if n == num + 1:
        st.print()
        return
    st.push(n)
    subsetsByStack(n + 1)
    st.pop()
    subsetsByStack(n + 1)
    return

def subsets(nums):
    result = []
    queue = Queue()
    # (현재 부분집합, 처리할 인덱스)
    queue.enqueue(([], 0))
    
    while queue:
        subset, idx = queue.dequeue()
        # 기저 사례: 모든 원소 처리 완료
        if idx == len(nums):
            result.append(subset)
        else:
            # 1) nums[idx]를 제외
            queue.enqueue((subset, idx + 1))
            # 2) nums[idx]를 포함
            queue.enqueue((subset + [nums[idx]], idx + 1))
    
    return result
    

if __name__ == "__main__":
    subsetsByStack(1)
    print(subsets([1, 2, 3]))
    