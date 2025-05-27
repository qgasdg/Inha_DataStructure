import array

class Sorter:
    def __init__(self, arr : array.array, n):
        self.array = arr
        self.size = n

    def printArray(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def quickSort(self, low, high):
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self.partition(low, high)

            # Recursively sort elements before partition and after partition
            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)
    
    def partition(self, low, high):
        # pivot (Element to be placed at right position)
        pivot = self.array[high]

        # Index of smaller element
        i = low - 1

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if self.array[j] <= pivot:
                i += 1
                # swap arr[i] and arr[j]
                temp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = temp

        # swap arr[i + 1] and pivot
        temp = self.array[i + 1]
        self.array[i + 1] = self.array[high]
        self.array[high] = temp
        return i + 1

def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6])
    sorter = Sorter(arr, n)
    sorter.printArray()
    sorter.quickSort(0, n - 1)
    sorter.printArray()

if __name__ == "__main__":
    main()