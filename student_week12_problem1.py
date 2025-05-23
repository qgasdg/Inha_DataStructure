import array
class LargestNumber:
    def __init__(self, arr : array.array, n):
        self.array = arr
        self.size = n
    
    def getDigits(self, number):
        digits = 0
        while number > 0:
            number //= 10
            digits += 1
        return digits

    def compare(self, a, b):
        '''=======Student's code======='''
    
    def quickSort(self, low, high):
        '''=======Student's code======='''
    
    def partition(self, low, high):
        '''=======Student's code======='''
    
    def largestNumber(self):
        '''=======Student's code======='''
        
def main():
    n = 5
    arr = array.array('h', [3, 30, 34, 5, 9])
    largestNumber = LargestNumber(arr, n)
    print(largestNumber.largestNumber()) # 9534330

    n = 3
    arr = array.array('h', [0, 0, 0])
    largestNumber = LargestNumber(arr, n)
    print(largestNumber.largestNumber()) # 0

if __name__ == "__main__":
    main()