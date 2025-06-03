import array

class Sorter:
    def __init__(self, arr : array.array, n):
        self.array = arr
        self.size = n

    def printArray(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def sort(self):
        self.array = self.quickSort(self.array, self.size)        

    def quickSort(self, arr, n):
        if n <= 1:
            return arr
        pivot = arr[n-1]
        L = array.array('h', [0] * (n-1))
        R = array.array('h', [0] * (n-1))
        L_index = 0
        R_index = 0
        # Partitioning the array by pivot
        for i in range(n-1):
            if arr[i] < pivot:
                L[L_index] = arr[i]
                L_index += 1
            else:
                R[R_index] = arr[i]
                R_index += 1
        # Recursively sort the left and right partitions
        L = self.quickSort(L, L_index)
        R = self.quickSort(R, R_index)
        # Combine the sorted partitions and pivot
        for i in range(L_index):
            arr[i] = L[i]
        arr[L_index] = pivot
        for i in range(R_index):
            arr[L_index + 1 + i] = R[i]
        return arr

def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6])
    sorter = Sorter(arr, n)
    sorter.printArray()
    sorter.sort()
    sorter.printArray()

if __name__ == "__main__":
    main()