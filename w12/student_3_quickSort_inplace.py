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
        '''=======Student's code======='''
        if low < high:
            pi = self.partition(low, high)

            self.quickSort(low, pi - 1)
            self.quickSort(pi + 1, high)
    
    def partition(self, low, high):
        '''=======Student's code======='''
        pivot = self.array[high]

        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                temp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = temp
        temp = self.array[i + 1]
        self.array[i + 1] = self.array[high]
        self.array[high] = temp
        return i + 1


def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6, 7])
    sorter = Sorter(arr, n)
    sorter.printArray()
    sorter.quickSort(0, n - 1)
    sorter.printArray()

if __name__ == "__main__":
    main()