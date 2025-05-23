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
        '''=======Student's code======='''
        if n == 0:
            return
        l, r = array.array('h', [0] * n), array.array('h', [0] * n)
        pivot = arr[n - 1]
        left, right = 0, 0
        for i in range(n - 1):
            if arr[i] < pivot:
                l[left] = arr[i]
                left += 1
            else:
                r[right] = arr[i]
                right += 1
        sorted_l, sorted_r = self.quickSort(l, left), self.quickSort(r, right)
        for i in range(left):
            l[i] = sorted_l[i]
        l[left] = pivot
        for i in range(right):
            l[left + i + 1] = sorted_r[i]
        return l


def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6])
    sorter = Sorter(arr, n)
    sorter.printArray()
    sorter.sort()
    sorter.printArray()

if __name__ == "__main__":
    main()