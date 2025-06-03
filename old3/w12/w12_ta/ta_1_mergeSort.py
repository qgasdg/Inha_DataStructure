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
        if l < r:
            # Divide the array into two halves
            m = (l + r) // 2
            self.mergeSort(l, m)
            self.mergeSort(m + 1, r)
            # Merge the sorted halves
            self.merge(l, m, r)


    def merge(self, l, m, r):
        # Copy data to temp arrays L[] and R[]
        L_n = m - l + 1
        R_n = r - m

        L = array.array('h', [0] * L_n)
        R = array.array('h', [0] * R_n)

        for i in range(L_n):
            L[i] = self.array[l + i]
        for j in range(R_n):
            R[j] = self.array[m + 1 + j]

        # Merge the temp arrays back into array[l..r]
        L_index = 0
        R_index = 0
        i = l

        while L_index < L_n and R_index < R_n:
            if L[L_index] <= R[R_index]:
                self.array[i] = L[L_index]
                L_index += 1
            else:
                self.array[i] = R[R_index]
                R_index += 1
            i += 1

        while L_index < L_n:
            self.array[i] = L[L_index]
            L_index += 1
            i += 1

        while R_index < R_n:
            self.array[i] = R[R_index]
            R_index += 1
            i += 1

def main():
    n = 5
    arr = array.array('h', [12, 11, 13, 5, 6])
    sorter = Sorter(arr, n)
    sorter.printArray() # 12 11 13 5 6 
    sorter.mergeSort(0, n - 1)
    sorter.printArray() # 5 6 11 12 13


if __name__ == "__main__":
    main()