class Node: # Tree Node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreorderTraversal(root): # Root, Left, Right
    if root: # Check if the node is not None
        print(root.data, end=' ')
        PreorderTraversal(root.left)
        PreorderTraversal(root.right)

def InorderTraversal(root): # Left, Root, Right
    if root: # Check if the node is not None
        InorderTraversal(root.left)
        print(root.data, end=' ')
        InorderTraversal(root.right)

def PostorderTraversal(root): # Left, Right, Root
    if root: # Check if the node is not None
        PostorderTraversal(root.left)
        PostorderTraversal(root.right)
        print(root.data, end=' ')

def main():
    # Create a binary tree
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Preorder Traversal
    PreorderTraversal(root) # 1 2 4 5 3 6 7
    print()

    # Postorder Traversal
    PostorderTraversal(root) # 4 5 2 6 7 3 1
    print()

    # Inorder Traversal
    InorderTraversal(root) # 4 2 5 1 6 3 7
    print()

if __name__ == '__main__':
    main()
