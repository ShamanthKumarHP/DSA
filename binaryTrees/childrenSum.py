class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    
    def childrenSum(self, root):
        if not root:
            return
        
        lc = 0
        rc = 0
        if root.left:
            lc = root.left.val
        if root.right:
            rc = root.right.val
        childs = lc + rc

        if root.val > childs:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val

        # go to left and right
        self.childrenSum(root.left)
        self.childrenSum(root.right)

        # once coming back check and add it to root
        root_Tot = 0
        if root.right:
            root_Tot = root_Tot + root.right.val
        if root.left:
            root_Tot = root_Tot + root.left.val
        
        # leaf node
        if root.right or root.left:
            root.val = root_Tot
        return root
def to_binary_tree(items):
    if not items:
        return None
    it = iter(items)
    root = Tree(next(it))
    q = [root]
    
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = Tree(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = Tree(val)
            q.append(node.right)
    return root

lst = [1,3,2,5,3,None,9]
root = to_binary_tree(lst)
TreeNode = Tree()
print(TreeNode.childrenSum(root))

# OR
TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)
