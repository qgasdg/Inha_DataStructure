from queue import Queue

def subsets(n):
    q = Queue()
    q.put([])  # 빈 집합으로 시작
    
    for i in range(1, n + 1):
        size = q.qsize()  # 현재 큐의 크기
        
        # 현재 큐에 있는 모든 부분집합에 대해
        for _ in range(size):
            curr_subset = q.get()
            
            # 현재 숫자를 포함하지 않는 부분집합
            q.put(curr_subset[:])
            
            # 현재 숫자를 포함하는 부분집합
            curr_subset.append(i)
            q.put(curr_subset)
    
    # 모든 부분집합 출력
    while not q.empty():
        print(*q.get())

# 테스트
if __name__ == "__main__":
    n = 3  # 1부터 3까지의 부분집합
    print(f"All subsets from 1 to {n}:")
    subsets(n)