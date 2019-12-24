class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lcaBinaryTree(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = lcaBinaryTree(root.left, p, q)
    right = lcaBinaryTree(root.right, p, q)

    if left and right:
        return root

    if left:
        return left
    if right:
        return right

    return None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

res = lcaBinaryTree(root, 2, 4)

print "LCA = ", res.val


