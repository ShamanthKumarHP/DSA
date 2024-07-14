class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    # ceil is >= key
    def ceil(self, root, key):
        ceil = -1
        while root:
            if root.val == key:
                ceil = root.val
                return ceil
            elif root.val > key:
                ceil = root.val
                root = root.left
            else:
                root = root.right
        
        return ceil
    
    # floor is <= key
    def floor(self, root, key):
        ceil = -1
        while root:
            if root.val == key:
                ceil = root.val
                return ceil
            elif root.val > key:
                root = root.left
            else:
                ceil = root.val
                root = root.right
        
        return ceil

TreeNode = Tree(5)
TreeNode.left = Tree(1)
TreeNode.right = Tree(7)
TreeNode.left.right = Tree(2)
TreeNode.left.right.right = Tree(3)

print(TreeNode.ceil(TreeNode, 4))
print(TreeNode.floor(TreeNode, 4))

