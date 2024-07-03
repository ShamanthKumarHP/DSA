# without stack space
# TC:  O(N)
# SC: O(1)
class Tree():
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
    # Left-Root-Right
    def inOrder_traversal(self, root):
        curr = root
        ans = []
        while curr != None:
            if curr.left is None:
                # which means i'm at root and no left sub tree so have to go right
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    # which means thread conneciton is not there, so establish
                    prev.right = curr
                    curr = curr.left
                elif prev.right == curr:
                    # which means connection is already there, so have break it move towards right
                    prev.right == None
                    ans.append(curr.val)
                    curr = curr.right
        return ans
    
    # Root-left-Right
    def preOrder_traversal(self, root):
        curr = root
        ans = []
        while curr != None:
            if curr.left is None:
                # which means i'm at root and no left sub tree so have to go right
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    # which means thread conneciton is not there, so establish
                    ans.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                elif prev.right == curr:
                    # which means connection is already there, so have break it move towards right
                    prev.right == None
                    curr = curr.right
        return ans

    
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


lst = [1,2,10,3,4,13,14]
root = to_binary_tree(lst)

ob = Tree()
print(ob.inOrder_traversal(root))
root = to_binary_tree(lst)
print(ob.preOrder_traversal(root))