import array


class LargestNumber:
    def __init__(self, arr: array.array, n):
        self.array = arr
        self.size = n

    def getDigits(self, number):
        digits = 0
        while number > 0:
            number //= 10
            digits += 1
        return digits

    def compare(self, a, b):
        """=======Student's code======="""
        # Convert numbers to strings and compare their concatenations
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        return int(ab) > int(ba)

    def quickSort(self, low, high):
        """=======Student's code======="""
        if low < high:
            # pi is partitioning index
            pi = self.partition(low, high)

            # Separately sort elements before and after partition
            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)

    def partition(self, low, high):
        """=======Student's code======="""
        pivot = self.array[high]

        # Index of smaller element
        i = low - 1

        # Compare all elements with pivot using custom comparison
        for j in range(low, high):
            if self.compare(self.array[j], pivot):
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        # Place pivot in its correct position
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def largestNumber(self):
        """=======Student's code======="""
        # Sort array using quicksort
        self.quickSort(0, self.size - 1)

        # Handle case where all numbers are 0
        if self.array[0] == 0:
            return "0"

        # Concatenate numbers to form result
        result = "".join(map(str, self.array))
        return result


def main():
    n = 5
    arr = array.array("h", [3, 30, 34, 5, 9])
    largestNumber = LargestNumber(arr, n)
    print(largestNumber.largestNumber())  # 9534330

    n = 3
    arr = array.array("h", [0, 0, 0])
    largestNumber = LargestNumber(arr, n)
    print(largestNumber.largestNumber())  # 0


if __name__ == "__main__":
    main()
