class Node:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None


max_sum = 0


def maxPathSum(node):
    global max_sum
    if node.rightChild is None and node.leftChild is None:
        return node.data

    left_max = maxPathSum(node.leftChild) if node.leftChild else float('-inf')
    right_max = maxPathSum(node.rightChild) if node.rightChild else float('-inf')

    if left_max + node.data + right_max > max_sum:
        max_sum = left_max + node.data + right_max

    return max(left_max, right_max) + node.data


def findMaxPathSum(root):
    global max_sum
    max_sum = float('-inf')
    maxPathSum(root)
    return max_sum


def main():
    #         1
    #       /   \
    #     -2     3
    #     / \   / \
    #    8  -1  4  -5

    """
    4개 중 2개 뽑기
    8 -2 -1 = 5
    8 -2 1 3 4 = 14 => 최대!
    8 -2 1 3 -5 = 5
    -1 -2 1 3 4 = 5
    -1 -2 1 3 -5 = -4
    4 3 -5 = 2
    """
    root = Node(1)
    root.leftChild = Node(-2)
    root.rightChild = Node(3)
    root.leftChild.leftChild = Node(8)
    root.leftChild.rightChild = Node(-1)
    root.rightChild.leftChild = Node(4)
    root.rightChild.rightChild = Node(-5)

    print(findMaxPathSum(root))

    # Output: 14 (8 + -2 + 1 + 3 + 4)

    #           -10
    #         /     \
    #       7         8
    #     /   \     /   \
    #   -5     2   1     12
    #  /  \              / \
    # 3   -4           -2   6
    #                         \
    #                          9

    root = Node(-10)
    root.leftChild = Node(7)
    root.rightChild = Node(8)

    root.leftChild.leftChild = Node(-5)
    root.leftChild.rightChild = Node(2)

    root.rightChild.leftChild = Node(1)
    root.rightChild.rightChild = Node(12)

    root.leftChild.leftChild.leftChild = Node(3)
    root.leftChild.leftChild.rightChild = Node(-4)

    root.rightChild.rightChild.leftChild = Node(-2)
    root.rightChild.rightChild.rightChild = Node(6)
    root.rightChild.rightChild.rightChild.rightChild = Node(9)

    print(findMaxPathSum(root)) # 36 (1 → 8 → 12 → 6 → 9)

if __name__ == "__main__":
    main()
