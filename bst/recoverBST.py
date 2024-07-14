# Definition for a binary tree node.
# https://leetcode.com/problems/recover-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev = None
    first = None
    last = None

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
                self.last = root
            else:
                self.last = root
        self.prev = root
        self.inorder(root.right)

    
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)
        if self.first and self.last:
            temp = self.last.val
            self.last.val = self.first.val
            self.first.val = temp

def to_binary_tree(items):
    if not items:
        return None
    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

lst = [1,3,None,None,2]
root = to_binary_tree(lst)
ob = Solution()
ob.recoverTree(root)
print(root)
    
    
        