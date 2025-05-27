import numpy as np


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class IntervalMerger:
    def __init__(self):
        self.capacity = 10000
        self.array = np.empty(self.capacity, dtype=object)
        self.size = 0

    def add(self, start, end):
        """=======Student's code======="""
        self.array[self.size] = Interval(start, end)
        self.size += 1

    def print(self):
        for i in range(self.size):
            print(f"[{self.array[i].start}, {self.array[i].end}]", end=" ")
        print()

    def mergeSort(self, l, r):
        """=======Student's code======="""
        if l < r:
            m = (l + r) // 2
            self.mergeSort(l, m)
            self.mergeSort(m + 1, r)
            self.merge(l, m, r)

    def merge(self, l, m, r):
        """=======Student's code======="""
        # Create temporary arrays
        n1 = m - l + 1
        n2 = r - m

        L = np.empty(n1, dtype=object)
        R = np.empty(n2, dtype=object)

        # Copy data to temporary arrays
        for i in range(n1):
            L[i] = self.array[l + i]
        for j in range(n2):
            R[j] = self.array[m + 1 + j]

        # Merge the temporary arrays back
        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i].start <= R[j].start:
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[] if any
        while i < n1:
            self.array[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[] if any
        while j < n2:
            self.array[k] = R[j]
            j += 1
            k += 1

    def intervalMerge(self):
        """=======Student's code======="""
        if self.size <= 1:
            return

        # Sort intervals based on start time
        self.mergeSort(0, self.size - 1)

        # Initialize merged array
        merged_index = 0

        for i in range(1, self.size):
            # If current interval overlaps with previous
            if self.array[merged_index].end >= self.array[i].start:
                # Update end of merged interval if needed
                self.array[merged_index].end = max(
                    self.array[merged_index].end, self.array[i].end
                )
            else:
                # No overlap, move to next position
                merged_index += 1
                self.array[merged_index] = self.array[i]

        # Update size to reflect merged intervals
        self.size = merged_index + 1


def main():
    merger = IntervalMerger()

    merger.add(1, 3)
    merger.add(2, 6)
    merger.add(8, 10)
    merger.add(15, 18)
    merger.intervalMerge()
    merger.print()  # [1, 6] [8, 10] [15, 18]


if __name__ == "__main__":
    main()
