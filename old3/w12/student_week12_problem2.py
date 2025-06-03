import array
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
        '''=======Student's code======='''
    
    def print(self):
        for i in range(self.size):
            print(f"[{self.array[i].start}, {self.array[i].end}]", end=" ")
        print()

    def mergeSort(self, l, r):
        '''=======Student's code======='''

    def merge(self, l, m, r):
        '''=======Student's code======='''

    def intervalMerge(self):
        '''=======Student's code======='''

def main():
    merger = IntervalMerger()
    
    merger.add(1, 3)
    merger.add(2, 6)
    merger.add(8, 10)
    merger.add(15, 18)
    merger.intervalMerge()
    merger.print() # [1, 6] [8, 10] [15, 18]

if __name__ == "__main__":
    main()