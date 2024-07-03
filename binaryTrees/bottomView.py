# line concept + level order

class Tree():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def bottomView(self, root):
        ans = []
        if not root:
            return ans
        
        virtus = dict()
        q = []
        q.append((root,0))

        while q:
            node, x = q.pop(0)

            # for a particular veritcal line, i have to insert first occurence 
            # first occurence is made sure as we are going level wise
            
            virtus[x] = node.val
            
            if node.left:
                q.append((node.left, x-1))

            if node.right:
                q.append((node.right, x+1))

        for values in sorted(virtus.items()):
            ans.append(values[1])
        return ans
    

TreeNode = Tree(2)
TreeNode.left = Tree(1)
TreeNode.left.left = Tree(3)
TreeNode.left.right = Tree(4)
TreeNode.right = Tree(10)
TreeNode.right.left = Tree(13)
TreeNode.right.right = Tree(14)


print(TreeNode.bottomView(TreeNode))
