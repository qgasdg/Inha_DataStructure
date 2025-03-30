def Hanoi(n, source = "A", destination = "C", auxiliary = "B"):
    #base case : n=1 
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    
    #n-1 디스크를 source에서 auxiliary로 옮기도록 재귀 호출
    Hanoi(n-1,source,auxiliary,destination)
    #n 디스크를 source에서 destination로 옮김
    print(f"Move disk {n} from source {source} to destination {destination}")
    #n-1 디스크를 auxiliary에서 destination로 옮기도록 재귀 호출
    Hanoi(n-1,auxiliary,destination,source)

def main():
    Hanoi(n = 5,source = "A", destination = "C", auxiliary = "B")
    # Move disk 1 from source A to destination C
    # Move disk 2 from source A to destination B
    # Move disk 1 from source C to destination B
    # Move disk 3 from source A to destination C
    # Move disk 1 from source B to destination A

if __name__ == '__main__':
    main()