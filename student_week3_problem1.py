# Node 클래스: 스택의 노드로, data에 저장할 값을 담고 다음 노드를 가리키는 next 포인터를 가짐.
class Node:
    def __init__(self, data):
        self.data = data   # 노드에 저장될 값 (여기서는 정수)
        self.next = None   # 다음 노드를 가리키는 포인터

# Stack 클래스: 연결 리스트를 기반으로 한 스택 구현
class Stack:
    def __init__(self):
        self.size = 0      # 스택에 저장된 원소의 개수
        self.top = None    # 스택의 최상단 노드를 가리킴

    def push(self, item):
        """
        push(item): 스택의 최상단에 새로운 원소(item)를 추가한다.
        """
        new_node = Node(item)  # 새 노드 생성
        self.size += 1         # 스택 크기 1 증가
        if not self.top:
            # 스택이 비어 있으면, 새 노드를 top으로 지정
            self.top = new_node
            return

        # 새 노드를 현재 top의 앞에 삽입 (LIFO 구조)
        new_node.next = self.top
        self.top = new_node
        return

    def pop(self):
        """
        pop(): 스택의 최상단 원소를 제거하고, 그 값을 반환한다.
        스택이 비어 있으면 None을 반환.
        """
        if not self.top:
            return None
        ret = self.top.data    # 반환할 데이터 저장
        self.top = self.top.next  # top을 다음 노드로 변경
        self.size -= 1         # 스택 크기 1 감소
        return ret

    def top(self):
        """
        top(): 스택의 최상단 원소를 반환한다.
        """
        return self.top

    def print(self):
        """
        print(): 스택의 모든 원소를 최상단부터 차례로 출력한다.
        """
        curr = self.top
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()
        return

    def is_empty(self):
        """
        is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환한다.
        """
        return self.size == 0

def reverse_number_with_stack(number):
    """
    reverse_number_with_stack(number):
    주어진 정수 number의 자릿수를 스택을 사용하여 역순으로 뒤집은 후,
    역순으로 뒤집은 정수를 반환한다.
    예를 들어, 125 -> 521
    """
    new_stack = Stack()
    # number의 각 자릿수를 스택에 push (숫자 % 10을 이용)
    while number:
        new_stack.push(number % 10)
        number //= 10

    ret = 0
    mul = 1
    # 스택이 빌 때까지 pop하면서 ret에 곱하여 더함 (역순 정수 생성)
    while not new_stack.is_empty():
        ret += new_stack.pop() * mul
        mul *= 10

    return ret

def is_palindrome(number):
    """
    is_palindrome(number):
    주어진 정수가 팰린드롬(앞뒤가 같은지)인지 검사하여, 맞으면 True, 아니면 False 반환.
    """
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
    # 테스트 예시: 정수를 뒤집어 팰린드롬 만드는 과정 확인
    # 주석 처리된 196는 팰린드롬이 생성되지 않는 예시.
    # palindrome_process(196)
    palindrome_process(125)
    palindrome_process(12321)
    palindrome_process(int(1e18))

if __name__ == "__main__":
    main()
