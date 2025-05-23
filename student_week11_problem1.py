import array


class Kth_largest:
    def __init__(self):
        self.capacity = 1000
        self.array = array.array("h", [0] * self.capacity)
        """=======Student's code======="""
        self.size = 0
        self.k = 0

    def findKthLargest(self, k, m, nums: array.array):
        """=======Student's code======="""
        # 1) k, size 초기화
        self.k = k
        # 첫 k개(또는 nums 전체 개수)만 heap에 담고
        if m < k:
            self.size = m
        else:
            self.size = k
        for i in range(self.size):
            self.array[i] = nums[i]
        # 2) min-heap으로 heapify
        for i in range((self.size - 1) // 2, -1, -1):
            self.downHeap(i)
        # 3) 나머지 원소들은 add()로 처리
        for i in range(self.size, m):
            self.add(nums[i])

    def add(self, item):
        """=======Student's code======="""
        # 아직 k개 미만이면 그냥 삽입 후 upHeap
        if self.size < self.k:
            self.array[self.size] = item
            self.size += 1
            self.upHeap(self.size - 1)
        # 이미 k개 이상이면, 루트(가장 작은 among top k)와 비교
        elif item > self.array[0]:
            self.array[0] = item
            self.downHeap(0)
        # k번째 큰 값은 항상 루트에
        return self.array[0]

    def downHeap(self, index):
        """=======Student's code======="""
        # min-heap 기준: 자식 중 더 작은 값이 부모보다 작으면 교환
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right

        if smallest != index:
            self.array[index], self.array[smallest] = (
                self.array[smallest],
                self.array[index],
            )
            self.downHeap(smallest)

    def upHeap(self, index):
        """=======Student's code======="""
        # min-heap 기준: 부모가 자식보다 크면 교환
        parent = (index - 1) // 2
        if index > 0 and self.array[parent] > self.array[index]:
            self.array[parent], self.array[index] = (
                self.array[index],
                self.array[parent],
            )
            self.upHeap(parent)


def main():
    print("1st test")
    kth = Kth_largest()
    nums = array.array("h", [4, 5, 8, 2])
    kth.findKthLargest(3, len(nums), nums)
    print(kth.add(3))  # 4
    print(kth.add(5))  # 5
    print(kth.add(10))  # 5
    print(kth.add(9))  # 8
    print(kth.add(4))  # 8

    print("2nd test")
    kth2 = Kth_largest()
    nums2 = array.array("h", [7, 7, 7, 7, 8, 3])
    kth2.findKthLargest(4, len(nums2), nums2)
    print(kth2.add(2))  # 7
    print(kth2.add(10))  # 7
    print(kth2.add(9))  # 7
    print(kth2.add(9))  # 8


if __name__ == "__main__":
    main()
