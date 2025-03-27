import array
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, item):
        new_node = Node(item)
        self.size += 1
        if not self.top:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node
        return

    def pop(self):
        if not self.top:
            return None
        ret = self.top.data # := return value
        self.top = self.top.next
        self.size -= 1
        return ret

    def top(self):
        return self.top

    def print(self):
        curr = self.top
        while curr:
            print(curr, end=' ')
            curr = curr.next
        print()
        return

    def is_empty(self):
        return self.size == 0

def reverse_number_with_stack(number):
    new_stack = Stack()
    while number:
        new_stack.push(number % 10)
        number //= 10

    ret = 0
    mul = 1
    while not new_stack.is_empty():
        ret += new_stack.pop() * mul
        mul *= 10

    return ret

def is_palindrome(number):
    return number == reverse_number_with_stack(number)

def palindrome_process(number, max_iterations=1000):
    iteration = 0
    print(f"Begin number: {number}")

    while not is_palindrome(number):
        reversed_num = reverse_number_with_stack(number)
        print(f"{number} + {reversed_num} = {number + reversed_num}")
        number += reversed_num
        iteration += 1

        if iteration > max_iterations:
            print("It's not a palindrome. stopping the process.")
            return None

    print(f"Final palindrome: {number} (repeats: {iteration})")
    return number

def main():
    # palindrome_process(196) # It's not a palindrome. stopping the process.
    palindrome_process(125)
    palindrome_process(12321)
    palindrome_process(int(1e18))

if __name__ == "__main__":
    main()