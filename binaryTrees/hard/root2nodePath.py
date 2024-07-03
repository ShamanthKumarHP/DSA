class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def root2node(self, root, target):
        if root is None:
            return []
        ds = []
        def recursion(node):
            if node is None:
                return False

            if node.left is None and node.right is None:
                if node.val == target:
                    ds.append(node.val)
                    return True
                return False
            
            ds.append(node.val)
            lt = recursion(node.left)
            rt = recursion(node.right)

            if lt or rt:
                return True

            ds.pop()
            return False
        
        recursion(root)
        return ds
TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)

print(TreeNode.root2node(TreeNode, 14))

