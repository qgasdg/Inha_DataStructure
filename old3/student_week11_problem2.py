import array
import numpy as np


class Exists:
    NOT_EXISTS = 0
    EXISTS = 1
    AVAILABLE = 2


class Item:
    def __init__(self, key, value):
        """=======Student's code======="""
        self.key = key
        self.value = value
        self.exists = Exists.EXISTS


class HashMap:
    def __init__(self, n, k):
        """=======Student's code======="""
        self.n = n
        self.k = k
        self.table = np.empty(n, dtype=Item)

    def hash(self, key):
        """=======Student's code======="""
        return key % self.n

    def putitem(self, key, value):
        """=======Student's code======="""
        initial_position = self.hash(key)
        position = initial_position

        while True:
            if (
                self.table[position] is None
                or self.table[position].exists != Exists.EXISTS
            ):
                self.table[position] = Item(key, value)
                return True

            position = (position + 1) % self.n
            if position == initial_position:
                return False

    def getCount(self, key):
        """=======Student's code======="""
        cnt = 0
        initial_position = self.hash(key)
        position = initial_position
        while True:
            if (
                self.table[position] is None
                or self.table[position].exists != Exists.EXISTS
            ):
                break
            elif self.table[position].value % self.k == key:
                cnt += 1

            position = (position + 1) % self.n

            if position == initial_position:
                break

        return cnt


class checker:
    def canArray(self, arr: array.array, n, k):
        """=======Student's code======="""
        if n % 2 != 0:  # Array length must be even : 배열 크기는 짝수여야 한다.
            return False

        # Create HashMap to store remainder counts : 나머지를 세기 위한 해시맵을 만든다.
        hmap = HashMap(n, k)

        # Count remainders : 나머지를 센다.
        for num in arr:
            rem = num % k
            hmap.putitem(rem, num)

        # Check if we can pair numbers : 수들을 짝 지을 수 있는지 확인한다.
        for i in range(k):
            if i == 0:
                # Numbers divisible by k should be even : k로 나누어 떨어지는 수의 개수는 짝수여야한다.
                if hmap.getCount(0) % 2 != 0:
                    return False
            elif i * 2 == k:
                # Numbers with remainder k/2 should be even : k/2인 애들은 짝수여야한다.
                if hmap.getCount(i) % 2 != 0:
                    return False
            else:
                # Check if count of remainder i equals count of remainder k-i :
                # 나머지가 i인 수와 k - i인 수의 개수가 같은지 확인한다.
                if hmap.getCount(i) != hmap.getCount(k - i):
                    return False

        return True


def main():
    c = checker()

    n = 4
    k = 6
    arr = array.array("h", [9, 7, 5, 3])
    if c.canArray(arr, n, k):  # YES
        print("YES")
    else:
        print("NO")

    n = 6
    k = 10
    arr = array.array("h", [92, 75, 65, 48, 45, 35])
    if c.canArray(arr, n, k):  # YES
        print("YES")
    else:
        print("NO")

    n = 4
    k = 10
    arr = array.array("h", [91, 74, 66, 48])
    if c.canArray(arr, n, k):  # NO
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
