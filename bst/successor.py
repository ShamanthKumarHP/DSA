class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

    def successor(self, root, key, ans):
        if not root:
            return None
        if root.val > key:
            ans[0] = root.val
            # print(ans)
            self.successor(root.left, key, ans)
        else:
            self.successor(root.right, key, ans)
    
    def predecessor(self, root, key, ans):
        if not root:
            return None
        if root.val >= key:
            self.predecessor(root.left, key, ans)
        else:
            ans[0] = root.val
            self.predecessor(root.right, key, ans)
    
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


# OR
TreeNode = Tree(5)
TreeNode.left = Tree(1)
TreeNode.right = Tree(7)
TreeNode.left.right = Tree(2)
TreeNode.left.right.right = Tree(3)

succesor = [None]
TreeNode.successor(TreeNode, 2, succesor)
print(succesor[0])

predeccesor=[None]
TreeNode.predecessor(TreeNode,2,predeccesor)
print(predeccesor[0])
