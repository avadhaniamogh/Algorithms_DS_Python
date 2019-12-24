class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def leftView(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while(len(queue) > 0):
        n = len(queue)
        for i in range(0, n):
            item = queue.pop(0)
            if i == 0:
                print item.val
            if item.left is not None:
                queue.append(item.left)
            if item.right is not None:
                queue.append(item.right)


root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(6)
root.right.left.right.left = TreeNode(18)
root.right.left.right.right = TreeNode(7)
leftView(root)



