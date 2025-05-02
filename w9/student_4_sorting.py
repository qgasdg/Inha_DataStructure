import array

class PrepareSorting:
    def __init__(self):
        self.capacity = 10
        self.array = array.array('h', [0]*self.capacity)

    def initalize(self):
        self.array[0] = 66
        self.array[1] = 48
        self.array[2] = 13
        self.array[3] = 5
        self.array[4] = 38
        self.array[5] = 9
        self.array[6] = 4
        self.array[7] = 3
        self.array[8] = 34
        self.array[9] = 75
    
    def display(self):
        for i in range(self.capacity):
            print(self.array[i], end = ' ')
        print()

    def insertion_sort(self):
        """=======Student's code======="""
        for i in range(self.capacity):
            for j in range(0, i):
                pass
    
    def bubble_sort(self):
        """=======Student's code======="""
        """이거 insertion 아닌가"""
        for i in range(self.capacity):
            for j in range(i, 0, -1):
                if self.array[j - 1] > self.array[j]:
                    self.array[j - 1], self.array[j] = self.array[j], self.array[j - 1]
                else:
                    break

def main():
    prepare = PrepareSorting()
    prepare.initalize()
    prepare.display()

    # Insertion Sort
    prepare.insertion_sort()
    prepare.display()

    prepare.initalize()

    # Bubble Sort
    prepare.bubble_sort()
    prepare.display()


if __name__ == '__main__':
    main()