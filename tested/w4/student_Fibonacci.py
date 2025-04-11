class Fibonacci:
    def recursive(self, n):
        if n == 0 or n == 1:
            return 1
        return self.recursive(n - 1) + self.recursive(n - 2)

    def iterative(self, n):
        ret, prev = 1, 1
        for i in range(n - 1):
            ret, prev = ret + prev, ret         
        return ret
    
    def linear_recursive(self, n):
        # print(n)
        if n == 0:
            return 0, 1
        if n == 1:
            return 1, 1
        fib = self.linear_recursive(n - 1)
        return fib[1], fib[1] + fib[0] # ret[1] is fibonacci(n)

def main():
    fibonacci = Fibonacci()
    print(fibonacci.recursive(5)) # 8
    print(fibonacci.iterative(5)) # 8
    print(fibonacci.linear_recursive(5)[1]) # 8
    inp = 1 # := input
    endp = int(input()) # := endpoint
    while inp != endp:
        # inp = int(input())
        print(fibonacci.linear_recursive(inp)[1])
        inp += 1

if __name__ == '__main__':
    main()