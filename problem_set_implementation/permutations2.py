from collections import deque

def permutations(n):
    def backtrack(path, used, stack):
        if len(path) == n:
            print(path)
            return
        
        for i in range(1, n + 1):
            if i not in used:
                stack.append(i)  # Push to stack
                used.add(i)
                backtrack(path + [i], used, stack)
                used.remove(i)
                stack.pop()

    stack = deque()
    backtrack([], set(), stack)

# Example usage
permutations(3)