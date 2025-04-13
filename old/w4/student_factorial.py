
class Factorial:
    def recursive(self, n):
        if n == 0:
            return 1
        return self.recursive(n - 1) * n
    
    def iterative(self, n):
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret
    
def main():
    factorial = Factorial()
    print(factorial.recursive(5)) # 120
    print(factorial.iterative(5)) # 120

if __name__ == '__main__':
    main()