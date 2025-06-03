import array
class Kth_largest:
    def __init__(self):
        self.capacity = 1000
        self.array = array.array('h', [0]*self.capacity)
        '''=======Student's code======='''


    def findKthLargest(self, k, m, nums: array.array):
        # Copy the values from nums to the array
        for i in range(m):
            self.array[i] = nums[i]
        '''=======Student's code======='''
        

    def add(self, item):
        '''=======Student's code======='''

    def downHeap(self, index):
        '''=======Student's code======='''
    
    def upHeap(self, index):
        '''=======Student's code======='''

def main():
    print("1st test")
    kth_largest = Kth_largest()
    nums = array.array('h', [4,5,8,2])
    k = 3
    m = 4
    kth_largest.findKthLargest(k, m, nums)
    print(kth_largest.add(3)) # 4
    print(kth_largest.add(5)) # 5
    print(kth_largest.add(10)) # 5
    print(kth_largest.add(9)) # 8
    print(kth_largest.add(4)) # 8

    print("2nd test")
    kth_largest2 = Kth_largest()
    nums2 = array.array('h', [7, 7, 7, 7, 8, 3])
    k2 = 4
    m2 = 6
    kth_largest2.findKthLargest(k2, m2, nums2)
    print(kth_largest2.add(2)) # 7
    print(kth_largest2.add(10)) # 7
    print(kth_largest2.add(9)) # 7
    print(kth_largest2.add(9)) # 8

if __name__ == '__main__':
    main()