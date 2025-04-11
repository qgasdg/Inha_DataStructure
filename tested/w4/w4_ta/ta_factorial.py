import time
class Factorial:
    def recursive(self, n):
        if n == 0:
            return 1
        return n * self.recursive(n - 1)
    
    def iterative(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
def main():
    factorial = Factorial()
    start_time = time.time()
    print(factorial.recursive(5)) # 120
    end_time = time.time()
    print(f"Recursive method took {end_time - start_time} seconds")

    start_time = time.time()
    print(factorial.iterative(5)) # 120
    end_time = time.time()
    print(f"Iterative method took {end_time - start_time} seconds")

if __name__ == '__main__':
    main()