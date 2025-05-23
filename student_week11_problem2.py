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
        self.table = [None] * n
        self.count = [0] * k  # Count for each remainder

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
                self.count[key] += 1
                return True

            position = (position + 1) % self.n
            if position == initial_position:
                return False

    def getCount(self, key):
        """=======Student's code======="""
        return self.count[key]


class checker:
    def canArray(self, arr: array.array, n, k):
        """=======Student's code======="""
        if n % 2 != 0:  # Array length must be even
            return False

        # Create HashMap to store remainder counts
        hmap = HashMap(n, k)

        # Count remainders
        for num in arr:
            rem = num % k
            hmap.putitem(rem, num)

        # Check if we can pair numbers
        for i in range(k):
            if i == 0:
                # Numbers divisible by k should be even
                if hmap.getCount(0) % 2 != 0:
                    return False
            elif i * 2 == k:
                # Numbers with remainder k/2 should be even
                if hmap.getCount(i) % 2 != 0:
                    return False
            else:
                # Check if count of remainder i equals count of remainder k-i
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
