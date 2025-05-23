import array

class Sorter:
    def __init__(self, arr : array.array, n):
        self.array = arr
        self.size = n

    def printArray(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

    def mergeSort(self, l, r):
        '''=======Student's code======='''
        if l == r:
            return
        mid = (l + r) // 2
        self.mergeSort(l, mid)
        self.mergeSort(mid + 1, r)
        self.merge(l, mid, r)

    def merge(self, l, m, r):
        '''=======Student's code======='''
        arr = array.array('h', [0]* (r - l + 1))
        left, right, idx = l, m + 1, 0
        while left <= m and right <= r:
            if self.array[left] <= self.array[right]:
                arr[idx] = self.array[left]
                left += 1
            else:
                arr[idx] = self.array[right]
                right += 1
            idx += 1
        while left <= m:
            arr[idx] = self.array[left]
            left += 1
            idx += 1
        while right <= r:
            arr[idx] = self.array[right]
            right += 1
            idx += 1

        for i in range(l, r + 1):
            self.array[i] = arr[i - l]

def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6, 7])
    sorter = Sorter(arr, n)
    sorter.printArray() # 12 11 13 5 6 
    sorter.mergeSort(0, n - 1)
    sorter.printArray() # 5 6 11 12 13


if __name__ == "__main__":
    main()