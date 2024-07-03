class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if root.left == None and root.right == None:
            return targetSum == 0
        lt = self.hasPathSum(root.left, targetSum - root.val)
        rt = self.hasPathSum(root.right, targetSum - root.val)
        return lt or rt


TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)

print(TreeNode.hasPathSum(TreeNode, 12))
