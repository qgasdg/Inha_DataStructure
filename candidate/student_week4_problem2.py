def findVisitOrder(n, x, y):
    if n == 1:
        dx, dy = (1, 0, 0, 1), (1, 1, 0, 0)
        for i in range(4):
            xx, yy = dx[i], dy[i]
            if x == xx and y == yy:
                return 1, i + 1
        return 0, 0
    ret = 0
    DIST = 2 ** (n - 1)
    dx, dy = (DIST, 0, 0, DIST), (DIST, DIST, 0, 0)
    for i in range(4):
        xx, yy = x - dx[i], y - dy[i]
        tmp = findVisitOrder(n - 1, xx, yy)
        pass
    return ret


def main():
    print(findVisitOrder(1, 1, 1)) # 1
    print(findVisitOrder(1, 0, 1)) # 2
    print(findVisitOrder(1, 0, 0)) # 3
    print(findVisitOrder(1, 1, 0)) # 4
    print(findVisitOrder(2, 1, 1)) # 9
    n_size = 3
    for y in range(2 ** n_size):
        for x in range(2 ** n_size):
            print("{:3n}".format(findVisitOrder(n_size, x, y)), end=' ')
        print()


if __name__ == '__main__':
    main()