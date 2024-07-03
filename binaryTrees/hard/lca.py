# https://www.youtube.com/watch?v=13m9ZCB8gjw
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# return object
class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    def lowestCommonAncestor(self, root, p, q):
        def recursion(node):
            if node is None:
                return None

            if (p ==  node.val) or (q == node.val):
                return node.val

            lt = recursion(node.left)
            rt = recursion(node.right)
            if lt and rt:
                return node.val
            elif not lt and not rt:
                return None
            return lt or rt
        return recursion(root)
        
        
    

TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)

print(TreeNode.lowestCommonAncestor(TreeNode, 14, 2))
