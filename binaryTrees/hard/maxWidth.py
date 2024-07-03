# https://www.youtube.com/watch?v=GLYXV-9F4AM 
# note
# https://leetcode.com/problems/maximum-width-of-binary-tree/
class Tree():
    def __init__(self, value=0):
        self.val = value
        self.left = None
        self.right = None

    def widthOfBinaryTree(self, root) :
        if not root:
            return 0
        
        q = []
        q.append(root)
        maxi = 0
        while q:
            size = len(q)
            lb = -1
            rb = -1
            for i in range(size):
                node = q.pop(0)
                if node is None:
                    q.append(None)
                    q.append(None)
                else:
                    if lb == -1:
                        lb = i
                    else:
                        rb = i
                    q.append(node.left)
                    q.append(node.right)
            maxi = max(maxi, rb-lb+1)
            if lb == -1 and rb == -1:
                break
            if lb+1 == rb:
                break

        return maxi
    
    def optimised_widthOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        
        q = []
        q.append((root, 0))
        maxi = 0
        while q:
            size = len(q)
            first_idx = q[0][1] # has idx of first element
            for i in range(size):
                node, curr_idx = q.pop(0)
                next_idx = curr_idx - first_idx

                if node.left:
                    q.append((node.left, (2*next_idx + 1)))

                if node.right:
                    q.append((node.right, (2*next_idx + 2)))
            maxi = max(maxi, (curr_idx - first_idx + 1))
    
        return maxi

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

# TreeNode = Tree(2)
# TreeNode.left = Tree(1)
# TreeNode.left.left = Tree(3)
# TreeNode.left.right = Tree(4)
# TreeNode.right = Tree(10)
# TreeNode.right.left = Tree(13)
# TreeNode.right.right = Tree(14)
TreeNode = Tree()
lst = [0,0,0,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None]

root = to_binary_tree(lst)
print(TreeNode.widthOfBinaryTree(root))