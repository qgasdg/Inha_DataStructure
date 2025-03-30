def findVisitOrder(n, x, y):
    # base case : n = 0, 탐색 순서에 대한 인덱스가 1부터 시작하므로 모든 값에 1을 더해야 함
    if n == 0:
        return 1

    # 한 변의 길이가 2^n인 정사각형을 네 쿼터로 나누는 코드
    quarter_size = 2 ** (n - 1)
    x_quarter = x // quarter_size
    y_quarter = y // quarter_size
    # 각 쿼터의 방문 순서는 앞서 진행한 쿼터를 모두 더해야 하므로 각 쿼터 길이의 제곱을 사용해야 함
    quarter_size_square = quarter_size ** 2
    dx, dy = (1, 0, 0, 1), (1, 1, 0, 0)

    # 쿼터의 위치에 따른 방문 순서 값을 더함. 재귀호출의 모듈러 연산은 quarter_size를 초과하는 행 또는 열 인덱스를 정규화하기 위함
    for i in range(4):
        if x_quarter == dx[i] and y_quarter == dy[i]:
            return quarter_size_square * i + findVisitOrder(n - 1, x % quarter_size, y % quarter_size)

def main():
    print(findVisitOrder(1, 1, 1))  # 1
    print(findVisitOrder(1, 0, 1))  # 2
    print(findVisitOrder(1, 0, 0))  # 3
    print(findVisitOrder(1, 1, 0))  # 4
    print(findVisitOrder(2, 1, 1))  # 9
    n_size = 3
    for y in range(2 ** n_size):
        for x in range(2 ** n_size):
            print("{:3n}".format(findVisitOrder(n_size, x, y)), end=' ')
        print()


if __name__ == '__main__':
    main()
