class Fibonacci:
    def fibonacci_recursive(self, n):
        if n <= 1:
            return 1
        return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)
    
    def fibonacci_iterative(self, n):
        if n <= 1:
            return 1
        prev = 1
        curr = 1
        for i in range(2, n+1):
            temp = curr
            curr += prev
            prev = temp
        return curr
    
def main():
    fibonacci = Fibonacci()
    print(fibonacci.fibonacci_recursive(5)) # 8
    print(fibonacci.fibonacci_iterative(5)) # 8

if __name__ == '__main__':
    main()